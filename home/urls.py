#This page is created by Pranav

from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from django.urls import path,include
from home import views
  
#Django admin header Costumization
admin.site.site_header = "Login as Pranav"
admin.site.site_title = "Admin_Pranav"
admin.site.index_title = "Welcome to Pranav's portal"

urlpatterns = [
   path('', views.home, name='home'),
   path('about', views.about, name='about'),
   path('info', views.info, name='info'),
   path('portfolio', views.portfolio, name='portfolio'),
   path('help', views.help, name='help')
]
