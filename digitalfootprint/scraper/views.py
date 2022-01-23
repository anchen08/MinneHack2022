from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InputForm
import requests

file = open('output.txt', 'w')
file.truncate(0)
# Create your views here.
def scraper(request):
    global context
    fname = mname = lname = phone = email = city = state = zip=""
    form = InputForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            #process data
            fname = form.cleaned_data.get("fname")
            mname = form.cleaned_data.get("mname")
            lname = form.cleaned_data.get("lname")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("phone")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            zip = form.cleaned_data.get("zip")

            list=[fname, mname, lname, phone, email, city, state, zip]
            for item in list:
                file.write(item)
                r = requests.get("https://serpapi.com/search.json?engine=google&q=" + item.replace(" ","+") + "&num=50&api_key=204efcd56a57bee1a50277f9f8fd5bdfe8ac4e45deb15d0e2d0c77afb0d15d88")
                r = r.json()
                if 'organic_results' in r:
                    for i in r['organic_results']:
                        if 'snippet' in i:
                            if item in i['snippet']:
                                file.write(i['title'] + "\n")
                                file.write(i['snippet'] + "\n")
                                file.write(i['link'] + "\n" + "\n")
            file.close()
            return HttpResponseRedirect('/')

    context = {'form':form, 'fname':fname, 'mname':mname, 'lname':lname, 'phone': phone, 'email': email, 'city':city, 'state':state, 'zip':zip}
    return render(request, 'index.html',context)
