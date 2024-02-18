from django.urls import path
from contactus import views

urlpatterns = [
    path('', views.contactus, name= 'contact-us'),
    path('register', views.user_register, name= 'user_register')
]