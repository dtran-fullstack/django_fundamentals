from django.db import models
from datetime import date

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Invalid Title"
        if len(postData['network']) < 3:
            errors["network"] = "Invalid Network"
        if len(postData['release']) == 0:
            errors["release"] = "Please input the release date!"
        elif postData['release'] > str(date.today()):
            errors["release"] = "Release date must be in the past"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Please provide more detail!"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)