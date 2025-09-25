# recipes/models.py
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()  # New field for recipe steps  # New field for recipe steps
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', blank=True, null=True)  # Field for image upload

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title