from django.db import models

# Create your models here.
class MakeDescriptionManager(models.Manager):
     def basic_validator(self, postData):
         errors = {}
         if len(postData['description']) < 15:
            errors['description'] = "Description should be at least 15 carecter"
         return errors
     
class MakeDescription(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MakeDescriptionManager()

    def __str__(self):
        return f'{self.description}'
    
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name should be at least five carecter"
        if len(postData['description']) < 15:
            errors['description'] = "Description should be at least 15 carecter"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=45)
    make_description = models.OneToOneField(MakeDescription,
                related_name="course",
                null=True,
                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return f'{self.id} {self.name} make_description_id:{self.make_description.id}' 