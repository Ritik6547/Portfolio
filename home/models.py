from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name + "->" + self.email

class Support(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    city = models.TextField()
    state = models.TextField()
    zip = models.CharField(max_length=6)
    query = models.TextField()

    def __str__(self):
        return self.firstname + " " + self.lastname + "-" + self.email