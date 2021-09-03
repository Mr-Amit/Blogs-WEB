# THIS IS LIKE TRIGGER IN DBMS 
# TO WORK IN THE DARK


# This is to automatically assign default profile
# picture to the user created
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# this decorator takes arguments, the signal and the sender
# when a user is saved, send the signal to this receiver
# which is the below function
# post_save passed to one of those is instance of the user
# and created (whether created or not)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        