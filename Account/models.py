from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choices=(('مذکر','آقا'),('مونث','خانم'))
    phone=PhoneNumberField( verbose_name='شماره تلفن',unique=True,default=None,null=True)
    Address = models.CharField(verbose_name = 'آدرس' ,max_length=100)
    Age = models.IntegerField(verbose_name = 'سن' , default=0)
    gender=models.CharField(verbose_name = 'جنسیت' , max_length=5,choices=gender_choices,default='مذکر')
    is_driver = models.BooleanField(verbose_name = 'وضعیت راننده بودن' , default=False)
    mellicode = models.CharField(verbose_name = 'کدملی' , max_length = 10)
    def __str__(self) -> str:
        return self.username