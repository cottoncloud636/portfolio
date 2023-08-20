#models.py is for storing data, related to the DB
from django.db import models


# Create your models here.
path1 = 'static/assets/media/'
class Project(models.Model): #inheriting functionality and features provided by the Model class from the 
                             #django.db.models
    screenshot = models.ImageField(upload_to=path1, blank=True, null=True)
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__ (self):
        return self.title


