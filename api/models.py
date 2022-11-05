from django.db import models
from Account.models import User
from django.utils import timezone
# Create your models here.
class reqtaxi(models.Model):
    CHOICES_TYPE = [
        ('Delivery', 'delivery'),
        ('Taxi', 'taxi'),
        ('Truck', 'truck'),
        ('Pickup_truck', 'pickup_truck'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    orig_addr = models.CharField(max_length=1000)
    dest_addr = models.CharField(max_length=1000)
    search_for_taxi = models.BooleanField(default = True)
    achieve_dest = models.BooleanField(default= False)
    create_time = models.DateTimeField(auto_now_add=True)
    travel_costs = models.IntegerField()
    type_travel = models.CharField(max_length=15,choices=CHOICES_TYPE , help_text='Insert type of travel')

    def __str__(self):
        return self.orig_addr  + '\t' + self.dest_addr + '\t' + str(self.travel_costs)