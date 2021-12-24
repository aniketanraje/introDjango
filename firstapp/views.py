from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.
def hello(request):
    return HttpResponse("hello from httpresponse")


def hello_from_html(request):
    return render(request, "hello.html")


def add(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]
    addition = int(num1) + int(num2)
    result = num1 + num2
    print("result:", result)
    context = {'concatedstring': result, 'addition': addition}
    return render(request, "result.html", context)
