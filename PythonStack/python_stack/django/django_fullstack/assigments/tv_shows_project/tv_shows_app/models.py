from django.db import models
import re

# Create your models here.
class ShowManager(models.Manager):
   def basic_validator(self, postData):
      errors = {}
      if len(postData['title']) < 2 :
           errors['title'] = "title should be at least two char"
      
      if len(postData['network']) < 2 :
           errors['network'] = "network should be at least two char"
      
      description = postData.get('description', '') 
      if description and len(description) < 10:
          errors['description'] = "description should be at least ten char"
      
      if not postData['release_date']:
           errors['release_date'] = "release date is required"
      
      return errors
   
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __str__(self):
        return f"{self.title}"