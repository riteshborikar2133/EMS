from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.profile import Profile
from django.contrib.auth.models import User

# Signal to create a Profile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the Profile when the User instance is saved (to keep them synchronized)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
