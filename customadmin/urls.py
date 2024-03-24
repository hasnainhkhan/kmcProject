from django.contrib import admin
from django.urls import path,include
# from customadmin import views
from customadmin.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('',admin_login,name = "admin_login"),
  path('dashboard',dashboard,name="dashboard"),
  path('Logout_Page',Logout_Page,name="log_out"),
  path('studentlist',Slist,name="rlist"),
  path('notice',NoTice,name="notice"),
  
]