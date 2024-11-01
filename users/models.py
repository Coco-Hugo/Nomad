from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        OTHER = ("other", "Other")
    
    first_name = models.CharField(max_length=50, editable = False,)
    last_name = models.CharField(max_length=50, editable = False,)
    profile_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank = True) # blank allows the field to be "not required"
    name = models.CharField(max_length=50, default = "",)
    gender = models.CharField(max_length=50, choices=GenderChoices.choices,)  
    
    def __str__(self):
        return self.username
    