from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InputForm

# Create your views here.
def scraper(request):
    if request.method == 'POST':
        print(request.GET)
        form = InputForm(request.POST)
        if form.is_valid():
            #process data
            fname = form.cleaned_data['fname']
            mname = form.cleaned_data['mname']
            lname = form.cleaned_data['lname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip = form.cleaned_data['zip']


            return HttpResponseRedirect('/')
    else:
        form = InputForm()

    return render(request, 'index.html',{'form':form})