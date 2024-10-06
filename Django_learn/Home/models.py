from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 12)
    lname = models.CharField(max_length=12)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=50)
    date = models.DateField()
    def __str__(self):
            return self.name

