from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("hello from httpresponse")

def hello_from_html(request):
    return render(request,"hello.html")