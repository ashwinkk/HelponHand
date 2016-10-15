from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=100)
	phonenum = models.CharField(max_length=15,primary_key=True)
	regid = models.CharField(max_length=250)