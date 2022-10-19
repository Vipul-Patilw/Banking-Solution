from django.contrib import admin
from django.urls import path
from . import  views
from Bank_Admin_Portal.registration_view import superusercreate
from Bank_Admin_Portal.userscreation_view import  usercreation_view

app_name = 'Bank_Admin_Portal'
urlpatterns = [
   path('',superusercreate.SuperUserCreate.as_view(),name='admin'),
   path('user-account',views.UserAccountCreate.as_view(),name='user-account'),
   path('users-detail',views.UsersDetail.as_view(),name='user-detail')
   ]