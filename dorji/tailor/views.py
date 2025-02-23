from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tailor index.")

def contact(request):
    return HttpResponse("This is the contact page.")

def about(request):
    return HttpResponse("This is the contact page.")