from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'announcements/home.html')

# Create your views here.
def about(request):
    return render(request , 'announcements/about.html')