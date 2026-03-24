from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100, blank=True)
    pet_age = models.IntegerField(blank=True, null=True)
    animal_health_certificate_valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class Vaccination(models.Model):

    VACCINE_CHOICES = [
        ('distemper', 'Distemper'),
        ('parvovirus', 'Parvovirus'),
        ('hepatitis', 'Hepatitis'),
        ('leptospirosis', 'Leptospirosis'),
        ('kennel_cough', 'Kennel Cough'),
        ('rabies', 'Rabies'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    vaccine_type = models.CharField(max_length=50, choices=VACCINE_CHOICES)
    date_given = models.DateField()

    next_due = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-calculate next due date
        if self.date_given:
            if self.vaccine_type == 'leptospirosis':
                self.next_due = self.date_given + timedelta(days=365)
            else:
                self.next_due = self.date_given + timedelta(days=365 * 3)

        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        from django.utils.timezone import now
        return self.next_due and self.next_due < now().date()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)