from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'announcements/home.html',context)

# Create your views here.
def about(request):
    return render(request , 'announcements/about.html',{'title': 'O nas'})