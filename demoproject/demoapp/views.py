from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Homepage(request):
    return render(request, "Homepage.html")

def About(request):
    return render(request, "About.html")

def contacts(request):
    return HttpResponse ("Contact number: 00000 00000")

def details(request):
    return render(request, "details.html")

def thankyou(request):
    return HttpResponse("Thank you")
