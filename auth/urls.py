from django.contrib import admin
from django.urls import include, path
from .import views
urlpatterns = [
    
    
    path('signup/', views.UserSignup , name = 'signup'),
    path('login/', views.UserLogin , name = 'login'),
    path('logout/', views.Userlogout , name = 'logout'),
    path('forgot-password/', views.forgot_password , name = 'forgot-password'),
    path('change-password/<token>/', views.ResetPassword , name = 'change-password'),
    path('', include("allauth.urls")),
]
