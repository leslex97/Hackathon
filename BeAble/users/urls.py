from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('login/', views.register, name='users-login'),
]