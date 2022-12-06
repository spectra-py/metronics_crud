from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from auth.models import CustomUsers
from blog.models import Post
from django.contrib import messages
# from .forms import UserUpdateForm
from django.urls import reverse
APP_THEME =  settings.APP_THEME
APP_VERSION =  settings.APP_VERSION
# Create your views here.


#Home-page view
def home_page(request):
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/home-index.html',{'APP_THEME': APP_THEME})

@login_required(login_url='/auth/login')
def dashboard_finance(request):
    current_user = request.user
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/index-finance.html',{'APP_THEME': APP_THEME,'current_user':current_user})

#profile page view
@login_required(login_url='/auth/login')
def profile(request):
    current_user = request.user
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/profile.html',{'APP_THEME': APP_THEME,'current_user':current_user})

# profile settings view
@login_required(login_url='/auth/login')
def profile_settings(request,id):
    current_user = request.user
    user = CustomUsers.objects.get(pk=id)
    if request.method == 'POST':
        
        first_name = request.POST.get('fname')
        middle_name = request.POST.get('middlename')
        username = request.POST.get('username')
        
        user = CustomUsers.objects.get(pk=id)
        user.first_name = first_name
        user.middle_name = middle_name
        user.username = username
        user.save()
        return redirect('/dashboard/profile/')
        
    
    
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/profile-settings.html',{'APP_THEME': APP_THEME,'current_user':current_user,'update': user})


def user_change_password(request,id):
    user = CustomUsers.objects.get(pk=id)
    
    if 'user-change-password' in request.method == 'POST':
        print("here")
        current_password = request.POST.get('currentpassword')
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmpassword')
        
        print( current_password)
        print( new_password)
        print( confirm_password )
        #validation check:
        #end validation check:
        
        user = CustomUsers.objects.get(pk=id)
        user.set_password(new_password)
        user.save()
        return redirect('/dashboard/profile/')
    
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/user-edit-password.html',{'APP_THEME': APP_THEME,'user-pass': user})
        

# users list view:
@login_required(login_url='/auth/login')
def users_list(request):
    if not request.user.is_superuser:
        return redirect('/dashboard/finance/')
    
    current_user = request.user
    users = CustomUsers.objects.exclude(is_superuser = True)
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/user-list.html',{'APP_THEME': APP_THEME,'users':users,'current_user': current_user})

# admin user data update view: 
@login_required(login_url='/auth/login')
def users_update(request,id):
    
    current_user = request.user
    user = CustomUsers.objects.get(pk=id)
    if request.method == 'POST':
        
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        
        
        user = CustomUsers.objects.get(pk=id)
        user.email = email
        user.username = username
        user.first_name = first_name
        user.middle_name = middle_name
        user.save()
        return redirect('/dashboard/users-list/')
        
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/user-update.html',{'APP_THEME': APP_THEME,'update': user,'current_user':current_user})


#admin chnage password view:
@login_required(login_url='/auth/login')
def password_update(request,id):
    
    user = CustomUsers.objects.get(pk=id)
    if  request.method == 'POST':
        user = CustomUsers.objects.get(pk=id)
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm-password')
        
        if  password != confirm_pass:
                messages.warning(request,'Password does not match',extra_tags='password')
                return HttpResponseRedirect('#')
        else:
            user.set_password(password)
            user.save(update_fields=['password'])
            return redirect('/dashboard/users-list/')
        
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/password-update.html',{'APP_THEME': APP_THEME,'update': user})

#admin user create:

def create_user(request):
    return render(request,'_templates/'+APP_THEME+'pages/dashboard/admin-user-create.html',{'APP_THEME': APP_THEME})


# delete user data view:

def delete_data(request, id):
    if request.method == 'POST':
        user = CustomUsers.objects.get(pk=id)
        user.delete()
        return HttpResponseRedirect('/dashboard/users-list/')