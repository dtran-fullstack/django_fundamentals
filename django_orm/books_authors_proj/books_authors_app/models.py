from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 0:
            errors['title'] = "Invalid Book Title"
        if len(postData['fname']) < 0 or len(postData['lname']) < 0:
            errors['name'] = "Invalid name"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def full_name(self):
        return self.fname + " " + self.lname