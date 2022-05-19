from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Profile

from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    # print('======', created)
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            email = user.email,
            username = user.username,
        )

@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
