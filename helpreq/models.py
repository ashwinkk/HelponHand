from django.db import models

# Create your models here.
class LocCache(models.Model):
	phonenum = models.CharField(max_length=15)
	lat = models.FloatField(max_length=20)
	lon = models.FloatField(max_length=20)