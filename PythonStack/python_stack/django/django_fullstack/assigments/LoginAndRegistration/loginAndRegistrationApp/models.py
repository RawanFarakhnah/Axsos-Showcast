from django.db import models
from datetime import datetime, timedelta
import bcrypt 
import re

# Create your models here.
class UserManger(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
           errors['first_name'] = "First name must be at least 2 alphabetic characters and contain only letters."
        
        if len(postData['last_name']) < 2 or not postData['first_name'].isalpha():
           errors['last_name'] = "Last name must be at least 2 alphabetic characters and contain only letters."
        
        if not postData.get('birthdate'):
           errors['empty_birth_date'] = "Please Enter a Birth Date"
        else:
           now = datetime.now()
           birth_date = datetime.strptime(postData.get('birthdate'), '%Y-%m-%d')
           min_age_date = now - timedelta(days=13 * 365)

           if birth_date > min_age_date:
               errors['birth_date'] = "Age must be greater than 13"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email address (e.g., user@example.com)."

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."

        if postData['confirm-password'] != postData['password']:
           errors['confirmPass'] = "Passwords do not match. Please ensure both passwords are identical."
       
        return errors
    
    def login_validator(self, postData):
        errors = {}
        try:
            this_user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), this_user.password.encode()):
                errors['login_validate'] = "Email or Password is not correct"
        except User.DoesNotExist:
            errors['DoesNotExist'] = "Email or Password is not correct"
        
        return errors
        



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    password = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManger()
