from django.db import models
from Account.models import User
from django.utils.text import slugify

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

    class Meta:
        verbose_name = 'درخواست ماشین' 
        verbose_name_plural = "درخواست های ماشین"

class TravelAddress(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    name = models.CharField(max_length = 250 , verbose_name='نام محل' , unique = True) 
    Address = models.CharField(max_length = 250 , verbose_name = 'آدرس')
    slug = models.SlugField(null = True , blank = True )

    def save(self, force_insert: bool = False , force_update: bool =False , using = None ,update_fields = None) -> None:
        self.slug = slugify(self.name)
        super(TravelAddress , self).save()

    def __str__(self) -> str:
        return f"username : {self.user.username}     Location : {self.name}"


    class Meta:
        verbose_name = ' آدرس های خاص' 
        verbose_name_plural = "  آدرس های خاص"
