from django.db.models.signals import post_save
from auth.models import CustomUsers
from django.dispatch import receiver
from .models import profile


@receiver(post_save,sender=CustomUsers)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)
        
        

@receiver(post_save,sender=CustomUsers)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
        
        