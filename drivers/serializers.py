from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import RequestCar
from api.serializers import RequestListSerializer
from .models import Driver_job


class Driver_jobserializer(ModelSerializer):
    def get_Auther(self , obj):
        return obj.user.username
    
    def get_travel_detail(self , obj ):
        return (
            obj.body.orig_addr,
            obj.body.dest_addr ,
            obj.body.travel_costs
        )
    body = RequestListSerializer()
    user =  serializers.SerializerMethodField(method_name='get_Auther')
    body = serializers.SerializerMethodField(method_name='get_travel_detail')
    class Meta:
        model = Driver_job
        fields = '__all__'

class Travel_serializer(ModelSerializer):
    class Meta:
        model = Driver_job
        fields = ('id' , 'body','time','finish','user')

class Travelcreat_serializer(ModelSerializer):
    body = serializers.PrimaryKeyRelatedField(queryset=RequestCar.objects.filter(search_for_taxi=True))
    class Meta:
        model = Driver_job
        fields = ('id' , 'body','time','user')