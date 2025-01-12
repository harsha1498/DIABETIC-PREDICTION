
from django.urls import path 
from . import views

urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('profile/<username>',views.profile,name='profile'),
    path('passwordrest',views.PasswordConfirm,name='PasswordRest'),


]