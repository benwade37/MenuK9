from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100, blank=True)
    pet_age = models.IntegerField(blank=True, null=True)
    vaccinations = models.TextField(blank=True)
    vaccination_date = models.DateField(blank=True, null=True)
    animal_health_certificate_valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)