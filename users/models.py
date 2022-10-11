from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    User profile database model
    """
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE)
    location = models.CharField(max_length=20, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    """
    Create a profile for the new user.
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
