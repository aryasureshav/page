from django.db import models

# Create your models here.
class Register(models.Model):
	Name=models.CharField(max_length=10,default='')
	Age=models.IntegerField(default='')
	Email=models.EmailField(default='')
	Password=models.CharField(max_length=8,default='')
	Photo=models.ImageField(upload_to='media/',default='')