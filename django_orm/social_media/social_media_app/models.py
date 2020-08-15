from django.db import models
import datetime
import re

# Create your models here.


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if postData['dob'] == "":
            errors['dob'] = "Please fill in date of birth!"
        elif postData['dob'] >= str(datetime.date.today()):
            errors['dob'] = "Invalid Date!!! Date of birth must be in the past!"
        else:
            input_year = postData['dob'][0:4]
            cur_date = str(datetime.date.today())
            cur_year = cur_date[0:4]
            if int(cur_year) - int(input_year) < 13:
                errors['dob'] = "User needs to be at least 13 to register"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_address'] = "Invalid email address"
        return errors

class OtherManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['length'] = "Message must be at least 5 characters!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def fullname(self):
        return self.first_name + " " + self.last_name


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OtherManager()


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OtherManager()
