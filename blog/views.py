from django.shortcuts import render
from django.http import HttpResponse
from website.settings import BASE_DIR

# Create your views here.
def name(request):
    return HttpResponse("this is my blog page")
    
def name1(request):
    print BASE_DIR
    return render(request,"anil.html",{})
