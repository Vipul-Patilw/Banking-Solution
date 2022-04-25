#pylint:disable=E0001
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import changePassword
urlpatterns = [
   path('sign',views.index, name='sign'),
   path('logininfo.html',views.index, name='sign'),
   path('home',views.home, name='home'),
   path('login',views.sign, name='login'),
   path('index.html',views.sign, name='login'),
   path('home',views.home, name='home'),
   path('practici45.html',views.home, name='home'),
   path('balance',views.balance, name='balance'),
   path('balance2.html',views.balance, name='balance'),
   path('setting.html',views.setting, name='setting'),
   path('balance copy 4.html',views.sendMoney, name='sendMoney'),
   path('send',views.sendMoney, name='sendMoney'),
   path('recharge',views.recharge, name='rechargeplan'),
   path('changePin.html',views.changePin, name='changePin'),
   path('recharge.html',views.recharge, name='rechargeplan'),
   path('operator.html',views.operator, name='operator'),
   path('about.html',views.about, name='about'),
   path('',views.lock, name='lock'),
   path('lock',views.lock, name='lock'),
   path('lock2',views.lock2, name='lock'),
   path('lock2.html',views.lock, name='lock'),
   path('lock.html',views.lock2, name='lock'),
   path('fgdf.html',views.privacy, name='privacyPolicy'),
   path('pass.html',changePassword.as_view(template_name='changePassword.html')),
 #  path('set',changePassword.as_view(template_name='resatePassword.html')),
   path('password_success',views.password_success, name='password_success'),
   path('ddd.html',views.personalDetails, name='personalDetails'),
   path('bank',views.bankDetails, name='bankDetails'),
   path('BankDetails2.html',views.bankDetails, name='bankDetails'),
   path('BankDetailsEdit.html',views.bankDetailsEdit, name='bankDetails'),
   path('withdraw.html',views.withdraw, name='withdraw'),
   path('logout',views.logoutuser, name='logout'),
   path('gotologin.html',views.gotologin, name='gotologin'),
   path('activate/<uidb64>/<token>',views.activate, name='activate'),
   path('change-password/{token}/',views.password_recovery, name='pass'),
   path('forgot-password',views.forgot_password, name='pass'),
   path('forgotPassword.html',views.forgot_password, name='forgotPassword'),

]

