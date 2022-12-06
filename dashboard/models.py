from email.policy import default
from django.db import models
from auth.models import CustomUsers

# Create your models here.



class profile(models.Model):
    user = models.OneToOneField(CustomUsers,on_delete=models.CASCADE)
    profile_picture = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    
    def __str__(self):
        return f'{self.user.email} Profile'