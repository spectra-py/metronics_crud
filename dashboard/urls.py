from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home_page,name='home-page'),
    path('finance/',views.dashboard_finance,name='finance'),
    path('profile/',views.profile,name='profile-page'),
    path('profile-settings/<int:id>/',views.profile_settings,name='settings'),
    path('users-list/',views.users_list,name='user'),
    path('delete/<int:id>/', views.delete_data, name = "deletedata"),
    path('user-update/<int:id>/',views.users_update,name='dataupdate'),
    path('add-user/',views.create_user,name='add-user'),
    path('password-update/<int:id>/',views.password_update,name='password-update'),
    path('password-change/<int:id>/',views.user_change_password,name='password-change'),
]


