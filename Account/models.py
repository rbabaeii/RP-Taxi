from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choices=(('مذکر','آقا'),('مونث','خانم'))
    phone=PhoneNumberField( verbose_name='شماره تلفن',unique=True,default=None,null=True)
    Address = models.CharField(max_length=100)
    Age = models.IntegerField(default=0)
    gender=models.CharField(max_length=5,choices=gender_choices,default='مذکر')
    is_driver = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.username