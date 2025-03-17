from django.db import models
import bcrypt
import re

# Create your models here.
class UserManger(models.Manager):
    def registor_validator(self, postData):
        errors = {}
        if len(postData.get('first_name')) < 2 or not postData.get('first_name').isalpha():
           errors['first_name'] = "First name should be at least 2 characters and only alphabetic."

        if len(postData.get('last_name')) < 2 or not postData.get('first_name').isalpha():
           errors['last_name'] = "Last name should be at least 2 characters and only alphabetic."

        EMAILREGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not EMAILREGEX.match(postData.get('email')):
           errors['email'] = "Enter a valid email (eg. user@example.com)"

        if not len(postData.get('password')) >= 8:
           errors['password'] = "Password should be at least 8 characters."
        
        if not postData.get('password') == postData.get('confirm_password'):
           errors['confirm_password'] = "Password  not match, please confirm password."
        
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
    password = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManger()

    

class CarManger(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        form_price = postData.get('price', '0')
        if form_price and not int(form_price) > 0 :
           errors['price'] = "Car price should be greater than zero."

        form_year = postData.get('year', '0')
        if form_year and not int(form_year) > 0 :
           errors['year'] = "Car year should be greater than zero."

        return errors

class Car(models.Model):
    price = models.IntegerField()
    model = models.CharField(max_length=45)
    make = models.CharField(max_length=45)
    year = models.IntegerField()
    seller = models.ForeignKey(User, related_name="cars", on_delete=models.CASCADE)
    seller_contact = models.CharField(max_length=45)
    purchaser = models.ForeignKey(User, related_name="purchas_cars", null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    status = models.BooleanField(default=False) #default is sold false
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarManger()

    def __str__(self):
        return f"{self.id} {self.model}"
