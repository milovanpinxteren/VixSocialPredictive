from django.db import models

# Create your models here.

class Banks(models.Model):
    bank_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class KeyWords(models.Model):
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=2000)