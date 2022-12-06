from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager




class CustomUsers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=255,default='')
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    forgot_password_token = models.CharField(max_length=100,default='')
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True,null = True , blank = True)
    updated_at = models.DateTimeField(auto_now=True,null = True , blank = True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
# user details model:

class Details(models.Model):
    
    user_id = models.ForeignKey(CustomUsers,on_delete=models.CASCADE)
    about = models.TextField()
    is_email_verified = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# # Roles model:
    
class Roles(models.Model):
    
    # user_id = models.OneToOneField(Users , on_delete=models.CASCADE)
    tittle = models.TextField(max_length=255)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'roles'
    
# # user_roles model:

class UserRoles(models.Model):
    
    user = models.OneToOneField(CustomUsers,on_delete=models.CASCADE)
    roles = models.ForeignKey(Roles,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_roles'