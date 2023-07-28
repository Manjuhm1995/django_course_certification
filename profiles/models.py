from django.db import models

# Create your models here.
class ProfileImages(models.Model):
    image=models.ImageField(upload_to="images")
