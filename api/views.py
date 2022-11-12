
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView , ListAPIView  , mixins
from .models import RequestCar
from .serializers import RequestListSerializer , RequestSerializer , TravelPriceSerailizer
from .permissions import IsOwnerOrAuthentication,IsSuperUserOrAuthentication


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

# class TravelPriceView(APIView):
#     def get_object(self , pk):
#         try:
#             return reqtaxi.objects.get(pk = pk)
#         except  reqtaxi.DoesNotExist:
#             raise Http404
#     def get(self , request ):
#         # queryset = self.get_object(pk)
#         taxi = reqtaxi.objects.all()
#         serializer = RequestListSerializer(taxi , many = True)
#         return Response(data = serializer.data)
#     def post(self , request):
#         data = request.data
#         serailizer = RequestSerializer(data=data)
#         if serailizer.is_valid():
#             serailizer.save()
#         return Response(data = data)