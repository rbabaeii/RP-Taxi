from rest_framework import serializers
from .models import RequestCar , TravelAddress

class RequestListSerializer(serializers.ModelSerializer):
    def get_author(self ,obj):
        return obj.user.username

    user = serializers.SerializerMethodField(method_name='get_author')
    class Meta:
        model = RequestCar
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta :
        model = RequestCar
        fields = '__all__'

class TravelPriceSerailizer(serializers.ModelSerializer):
    class Meta:
        model = RequestCar
        fields = ('travel_costs')

class ListTravelAdressSerializer(serializers.ModelSerializer):

    def get_author(self ,obj):
        return obj.user.username

    user = serializers.SerializerMethodField(method_name='get_author')

    class Meta :
        model = TravelAddress
        fields = '__all__'

class CreateTravelAdressSerializer(serializers.ModelSerializer):
    class Meta :
        model = TravelAddress
        fields = ('user', 'name' , 'Address')

class UpdateTravelAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAddress
        fields = ('name' , 'Address')