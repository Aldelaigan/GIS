from django.db import models

# Create your models here.

class Mapping(models.Model):
    user = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    date_created = models.DateTimeField()
    last_modified = models.DateTimeField()
    governate = models.CharField(max_length=120)
    area = models.CharField(max_length=120)
    block = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    house = models.CharField(max_length=120)
    paci_serial = models.CharField(max_length=120)
    land_size = models.CharField(max_length=120)

def __str__(self):
    return self.user
