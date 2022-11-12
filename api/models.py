from django.db import models
from Account.models import User

# Create your models here.
class RequestCar(models.Model):
    CHOICES_TYPE = [
        ('Delivery', 'پیک'),
        ('Taxi', 'تاکسی'),
        ('Truck', 'کامیون'),
        ('Pickup_truck', 'وانت'),
    ]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    orig_addr = models.CharField(verbose_name='آدرس مبدا',max_length=200)
    dest_addr = models.CharField(verbose_name='ادرس مقصد',max_length=200)
    search_for_taxi = models.BooleanField(verbose_name='درحال جست و جو برای تاکسی',default = True)
    achieve_dest = models.BooleanField(verbose_name='رسیده به مقصد',default= False)
    create_time = models.DateTimeField(verbose_name='زمان ساخت',auto_now_add=True)
    travel_costs = models.IntegerField(verbose_name='هزینه سفر')
    type_travel = models.CharField(verbose_name='نوع سفر',max_length=15,choices=CHOICES_TYPE , help_text='Insert type of travel')

    def __str__(self):
        return f'{self.orig_addr } {self.dest_addr}  {self.type_travel} {str(self.travel_costs)}' 
