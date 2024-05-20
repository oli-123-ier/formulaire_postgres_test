from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    lieu_habitation = models.CharField(max_length=200)

    def __str__(self):
        return self.name
