from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Srikanth'})


def add(request):
    val=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val+val2
    return render(request,'result.html',{'result':res})
