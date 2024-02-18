from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
# Create your views here.

def contactus(request):
    return render(request,'contactus/contactus_page.html')

def user_register(request):
    if request.method=="POST":
        form_register=UserRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password_1'])
            return redirect('home:home-func')
    else:
        form_register=UserRegisterForm()
        context={'form_register':form_register}
        return render(request, 'contactus/user_register.html',context)