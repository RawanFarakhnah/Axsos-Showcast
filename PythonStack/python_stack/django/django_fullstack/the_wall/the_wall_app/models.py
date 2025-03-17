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


class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if not postData.get('message'):
           errors['message'] = 'No message to post. Please type something before possting.'
        return errors

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if not postData.get('comment'):
           errors['comment'] = 'No comment to post. Please type something before possting.'
        return errors

class Comment(models.Model):
    created_by_user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="message_comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()