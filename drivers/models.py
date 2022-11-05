from django.db import models
from Account.models import User
from api.models import reqtaxi
from django.utils import timezone
# Create your models here.


class Driver_job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.ForeignKey(reqtaxi , on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=timezone.now)
    finish = models.BooleanField(default=False)