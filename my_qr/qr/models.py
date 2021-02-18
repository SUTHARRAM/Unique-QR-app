from django.db import models

# Create your models here.
class Soap(models.Model):
    ''' Storing detail about soap'''
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name