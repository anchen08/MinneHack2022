from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InputForm

# Create your views here.
def hello_test(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            #process data
            return HttpResponseRedirect('/')
    else:
        form = InputForm()
    print(request.GET)
    return render(request, 'form.html',{'form':form})