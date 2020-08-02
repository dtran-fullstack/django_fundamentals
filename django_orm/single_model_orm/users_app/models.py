from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['age'] < 0:
            errors['age'] = "Invalid age"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

