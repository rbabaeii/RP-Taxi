from .serializers import UserSerializer , BalanceSerializer , PayTravelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView  
from rest_framework.views import APIView
from .permissions import Is_StaffOrAdminReadonly , IsSuperUser
from rest_framework.viewsets import ModelViewSet
from django.db import transaction
from django.db.models import F
from .models import User
from api.models import RequestCar
from django.http import Http404

# Create your views here.
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (Is_StaffOrAdminReadonly,)
    search_fields = ['user__username']

class AddBalanceapiview(APIView):
    def put(self , request , pk):
        serializer = BalanceSerializer(data = request.data)
        if serializer.is_valid():
            user = User.objects.get(id = request.user.id)
            user.account_balance += serializer.validated_data.get('account_balance')
            user.save()
            return Response({"your account Charged  your balance is = "f'{user.account_balance}'} )
class PayTravel(APIView):
    def get_object(self , pk):
        try:
            return RequestCar.objects.get(id = pk)
        except RequestCar.DoesNotExist:
            raise Http404

    def get(self , request , pk):
        model = self.get_object(pk)
        serializer = PayTravelSerializer(model)
        return Response(data = serializer.data)

    def put(self , request , pk):
        model = self.get_object(pk)
        user = User.objects.get(id = request.user.id)
        if user.account_balance >= model.travel_costs:
            user.account_balance -= model.travel_costs
            user.save()
            return Response({"Paymeny Succesfull Goodluck"} , status= status.HTTP_202_ACCEPTED)
        else:
            return Response({'You have not Enough Money Please Rechage your Account'} , status=status.HTTP_400_BAD_REQUEST)