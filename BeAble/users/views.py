from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, FormView
from .forms import UserRegisterForm, UserInfoForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username= obj.email.split('@')[0]
            obj.save()
            
            messages.success(request, f'Konto utworzone. Zaloguj sie')
            new_user = authenticate(
                                username=obj.username,
                                password=form.cleaned_data['password1'],
                                    )  
            login(request, new_user)
            return redirect('profile_info')
    else:
        form = UserRegisterForm()       

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def profile_info(request):
    current_user = request.user.id
    form = UserInfoForm(request.POST)
    form.user = current_user
    model = Disabled_info(**form.cleaned_data)
    if request.method == 'POST':
            obj = model
            obj.save()
            form.user_id= current_user
            
            return redirect('profile')
    else:
        form = UserInfoForm()
        
    return render(request, 'users/profile_info.html',{'current_user': current_user, 'form': form})
    

