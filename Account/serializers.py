from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from allauth.account.adapter import get_adapter
from api.models import RequestCar

class CustomeRegisterSerilizer(RegisterSerializer):
    phone = serializers.CharField()
    Address = serializers.CharField()
    Age = serializers.IntegerField()
    gender = serializers.CharField()
    is_driver = serializers.BooleanField(default=False)
    mellicode = serializers.CharField()
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone': self.validated_data.get('phone'),
            'Address': self.validated_data.get('Address'),
            'Age': self.validated_data.get('Age'),
            'gender': self.validated_data.get('gender'),
            'is_driver': self.validated_data.get('is_driver'),
            'mellicode' : self.validated_data.get('mellicode'),
        }
    def save(self,request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.phone = self.cleaned_data.get('phone')
        user.Address = self.cleaned_data.get('Address')
        user.Age = self.cleaned_data.get('Age')
        user.gender = self.cleaned_data.get('gender')
        user.is_driver = self.cleaned_data.get('is_driver')
        user.mellicode = self.cleaned_data.get('mellicode')
        user.save()
        adapter.save_user(request , user , self)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('account_balance' ,)

class PayTravelSerializer(serializers.ModelSerializer):
    class Meta :
        model = RequestCar
        fields = ('travel_costs',)