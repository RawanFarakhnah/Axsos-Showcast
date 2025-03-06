from django.db import models

# Create your models here.
class Dojo(models.Model):
      name = models.CharField(max_length=255)
      city = models.CharField(max_length=255)
      state = models.CharField(max_length=2)
      desc = models.TextField(null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return f"{self.name}, {self.city}, {self.state}"

class Ninja(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return f"{self.first_name}, {self.last_name}"

