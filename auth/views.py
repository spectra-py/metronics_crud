from email.mime import message
from webbrowser import get
from django.shortcuts import render,redirect
import requests
from .models import CustomUsers
from django.contrib import messages
from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control
from .helpers import send_forgot_password_mail
import uuid
import json
APP_THEME =  settings.APP_THEME
APP_VERSION =  settings.APP_VERSION


# Create your views here.

#user signup view:
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def UserSignup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/finance')
    if request.method == 'POST':
        
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_password')
        
        #validation check
        if  password != confirm_pass:
                messages.error(request,'Password does not match',extra_tags='pass')
                return redirect('/auth/signup/')
            
        elif CustomUsers.objects.filter(email=email).exists():
                messages.warning(request,'email already exists',extra_tags='mail')
                return redirect('/auth/signup/')
            
        #end validtaion check
        data = CustomUsers.objects.create_user(email=email,username = username,first_name = first_name,middle_name = middle_name,password = password)
        data.save()
        
        # profile_obj = Profile.objects.create(user = data)
        # profile_obj.save()
        return redirect('/auth/login')
    
    else:
           
        return render(request,'_templates/'+APP_THEME+'pages/auth/signup.html',{'APP_THEME': APP_THEME})
    
    
    
# User login view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/finance')
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #recaptcha function:
        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LdNHFkiAAAAAHNJtarENxgE-Z235MRwCJvLGVM2'
        captchaData = {
            'secret': secretKey,
            'response': clientKey
        }
        
        r= requests.post('https://www.google.com/recaptcha/api/siteverify',data = captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('you success is :', verify)
        #end reCapTcha
        
        user = auth.authenticate(email = email , password = password)
        
        if user is not None and verify is not False:
            auth.login(request,user)
            return redirect('/dashboard/finance')
        if verify is False:
            return redirect('/auth/login/')
        else:
            messages.info(request,'invalid credentials',extra_tags='accnt')
            return redirect('/auth/login/')
        
    else:
        
        return render(request,'_templates/'+APP_THEME+'pages/auth/login.html',{'APP_THEME': APP_THEME})
            
  

#forgot password view:            
def forgot_password(request):
    try:
    
        if request.method == 'POST':
            email = request.POST.get('email')
            print("here in if")
            
            if not CustomUsers.objects.filter(email=email).first():
                messages.error(request,'No user found with this email',extra_tags='forgot')
                return redirect('/auth/forgot-password')
            
            user_obj = CustomUsers.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj = CustomUsers.objects.get(email=user_obj)
            profile_obj.forgot_password_token = token
            profile_obj.save()
            send_forgot_password_mail(user_obj.email,token)
            messages.success(request,'done')
            return redirect('/auth/forgot-password')
        
    except Exception as e:
        print(e)
    return render(request,'_templates/'+APP_THEME+'pages/auth/forgot-password.html',{'APP_THEME': APP_THEME})

#Reset password view:
def ResetPassword(request,token):
    context = {}
    try:
        user_obj = CustomUsers.objects.get(forgot_password_token = token )
        
        if request.method == 'POST':
            new_password = request.POST.get('new-password')
            confirm_password = request.POST.get('confirm-password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.error(request,'No user found',extra_tags='user_none')
                return redirect(f'/auth/change-password/{token}/')
            
            if new_password != confirm_password:
                messages.error(request,'Password does not match',extra_tags='pass_error')
                return redirect(f'/auth/change-password/{token}/')
        
            user_obj = CustomUsers.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/auth/login/')
        
        
    except Exception as e:
        print(e)
    return render(request,'_templates/'+APP_THEME+'pages/auth/change-password.html',{'APP_THEME': APP_THEME,'user_id': user_obj.id})


#User Signout view:
@login_required(login_url='/auth/login')     
def Userlogout(request):
    
    logout(request)
    return render(request,'_templates/'+APP_THEME+'pages/auth/logout.html',{'APP_THEME': APP_THEME})