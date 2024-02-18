
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
    path('contactus/',include('contactus.urls')),
    path('home/', include ('home.urls', namespace='home'))
]
