from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # When the room is created, the date is set
    updated_at = models.DateTimeField(auto_now=True) # When the room is saved, the date is set
    
    # Django will look at this and not put it in the DB because it should not be in the admin panel
    class Meta:
        abstract = True
    
    def __str__(self):
        pass
    