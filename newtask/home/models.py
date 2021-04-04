from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import signals

# Create your models here.

status = [("Active","Active"),("Inactive","Inactive"),("Delete","Delete")]
roles = [('Admin','Admin'),('Employee','Employee'),('Student','Student'),('Manager','Manager')]


class User(AbstractUser):
	image = models.ImageField(upload_to='user/', blank=True, null=True)
	mobile = models.CharField(max_length = 100, null = True, blank = True, default = '')
	user_type = models.CharField(max_length=10, choices=roles, default='Employee')
	role = models.CharField(max_length=50,choices=roles,default='Customer')
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "01. User"

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name

# from .decorators import user_task
# @user_task(signals.post_save.connect)
# class Usave(models.Model):
# 	signals.post_save.connect(user_task, sender=User)

class Employee(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	designation = models.CharField(max_length= 255 )
	salary = models.CharField(max_length= 255 )
