from rest_framework import serializers
from .models import reqtaxi
class RequestListSerializer(serializers.ModelSerializer):
    def get_author(self ,obj):
        return obj.user.username

    user = serializers.SerializerMethodField(method_name='get_author')
    class Meta:
        model = reqtaxi
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta :
        model = reqtaxi
        fields = '__all__'