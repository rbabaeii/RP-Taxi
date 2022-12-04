
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView , ListAPIView  , CreateAPIView 
from .models import RequestCar , TravelAddress
from .serializers import RequestListSerializer , RequestSerializer , ListTravelAdressSerializer , CreateTravelAdressSerializer , UpdateTravelAddressSerializer
from .permissions import IsOwnerOrAuthentication,IsSuperUserOrAuthentication , IsownerOrstaff
from rest_framework import status

# Taxi Views
class RequestTaxiList(ListAPIView):
    queryset = RequestCar.objects.filter(type_travel='Taxi')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)
    filterset_fields = ['orig_addr' , 'user__username']
    search_fields = ['orig_addr', 'user__username']
    ordering_fields = ['create_time' , 'travel_costs']  
    
class ActiveRequsetTaxi(ListCreateAPIView):
    queryset = RequestCar.objects.filter(type_travel='Taxi' , search_for_taxi=True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)
    filterset_fields = ['orig_addr' , 'user__username']
    search_fields = ['orig_addr', 'user__username']
    ordering_fields = ['create_time' , 'travel_costs']  


class RequestTaxiDetail(RetrieveUpdateDestroyAPIView):
    queryset = RequestCar.objects.filter(type_travel='Taxi')
    serializer_class = RequestListSerializer
    permission_classes = (IsOwnerOrAuthentication,)
    filterset_fields = ['orig_addr' , 'user__username']
    search_fields = ['orig_addr', 'user__username']
    ordering_fields = ['create_time' , 'travel_costs']  



# Delivery Views

class RequestDeliveryList(ListAPIView):

    queryset = RequestCar.objects.filter(type_travel='Delivery')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)

class ActiveRequsetDelivery(ListCreateAPIView):
    queryset = RequestCar.objects.filter(type_travel='Delivery' , search_for_taxi=True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class RequsetDeliveryDetail(RetrieveUpdateDestroyAPIView):
    queryset = RequestCar.objects.filter(type_travel='Delivery')
    serializer_class = RequestSerializer
    permission_classes = (IsOwnerOrAuthentication,)



# Truck Views
class RequestTruckList(ListAPIView):
    queryset = RequestCar.objects.filter(type_travel='Truck')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class ActiveRequestTruck(ListCreateAPIView):
    queryset = RequestCar.objects.filter(type_travel = 'Truck',search_for_taxi = True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class RequestTruckDetail(RetrieveUpdateDestroyAPIView):
    queryset = RequestCar.objects.filter(type_travel ='Truck')
    serializer_class = RequestSerializer
    permission_classes = (IsOwnerOrAuthentication,)

# Pickup_truck Views
class RequestPickup_truckList(ListAPIView):
    queryset = RequestCar.objects.filter(type_travel='Pickup_truck')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class ActiveRequestPickup_truck(ListCreateAPIView):
    queryset = RequestCar.objects.filter(type_travel = 'Pickup_truck',search_for_taxi = True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class RequestPickup_truckDetail(RetrieveUpdateDestroyAPIView):
    queryset = RequestCar.objects.filter(type_travel ='Pickup_truck')
    serializer_class = RequestSerializer
    permission_classes = (IsOwnerOrAuthentication,)


class ListTravelAddress(APIView):

    permission_classes = (IsownerOrstaff ,)

    def get_object(self , pk ,slug):
        try:
            return TravelAddress.objects.get(user__pk = pk , slug = slug)
        except TravelAddress.DoesNotExist:
            raise Http404
    

    def get(self , request ,pk ,slug):
    
        queryset = self.get_object(pk ,slug)
        serializer = ListTravelAdressSerializer(queryset)

        return Response(serializer.data , status = status.HTTP_200_OK)
    def put(self , request , pk , slug):
        serializer = UpdateTravelAddressSerializer(data = request.data)
        if serializer.is_valid():
            queryset = self.get_object(pk , slug)
            queryset.name = serializer.validated_data.get('name')
            queryset.Address = serializer.validated_data.get('Address')
            queryset.save()
            return Response({'msg':'Update Succesfull'} , status = status.HTTP_202_ACCEPTED)

            
class CreateTravelAddress(CreateAPIView):
    queryset = TravelAddress.objects.all()
    serializer_class = CreateTravelAdressSerializer
    permission_classes = (IsownerOrstaff , )