from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView , ListAPIView
# from taxiapp.views import req_taxi
from .models import reqtaxi
from .serializers import RequestListSerializer , RequestSerializer
from .permissions import IsOwnerOrAuthentication,IsSuperUserOrAuthentication


# Taxi Views
class RequestTaxiList(ListAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Taxi')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)
    filterset_fields = ['orig_addr' , 'user__username']
    search_fields = ['orig_addr', 'user__username']
    ordering_fields = ['create_time' , 'travel_costs']  
    
class ActiveRequsetTaxi(ListCreateAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Taxi' , search_for_taxi=True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)
    filterset_fields = ['orig_addr' , 'user__username']
    search_fields = ['orig_addr', 'user__username']
    ordering_fields = ['create_time' , 'travel_costs']  


class RequestTaxiDetail(RetrieveUpdateDestroyAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Taxi')
    serializer_class = RequestListSerializer
    permission_classes = (IsOwnerOrAuthentication,)
    filterset_fields = ['orig_addr' , 'user__username']
    search_fields = ['orig_addr', 'user__username']
    ordering_fields = ['create_time' , 'travel_costs']  



# Delivery Views

class RequestDeliveryList(ListAPIView):

    queryset = reqtaxi.objects.filter(type_travel='Delivery')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)

class ActiveRequsetDelivery(ListCreateAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Delivery' , search_for_taxi=True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class RequsetDeliveryDetail(RetrieveUpdateDestroyAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Delivery')
    serializer_class = RequestSerializer
    permission_classes = (IsOwnerOrAuthentication,)



# Truck Views
class RequestTruckList(ListAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Truck')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class ActiveRequestTruck(ListCreateAPIView):
    queryset = reqtaxi.objects.filter(type_travel = 'Truck',search_for_taxi = True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class RequestTruckDetail(RetrieveUpdateDestroyAPIView):
    queryset = reqtaxi.objects.filter(type_travel ='Truck')
    serializer_class = RequestSerializer
    permission_classes = (IsOwnerOrAuthentication,)

# Pickup_truck Views
class RequestPickup_truckList(ListAPIView):
    queryset = reqtaxi.objects.filter(type_travel='Pickup_truck')
    serializer_class = RequestListSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class ActiveRequestPickup_truck(ListCreateAPIView):
    queryset = reqtaxi.objects.filter(type_travel = 'Pickup_truck',search_for_taxi = True)
    serializer_class = RequestSerializer
    permission_classes = (IsSuperUserOrAuthentication,)


class RequestPickup_truckDetail(RetrieveUpdateDestroyAPIView):
    queryset = reqtaxi.objects.filter(type_travel ='Pickup_truck')
    serializer_class = RequestSerializer
    permission_classes = (IsOwnerOrAuthentication,)
