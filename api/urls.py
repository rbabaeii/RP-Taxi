from django.urls import path
from .views import (ActiveRequsetTaxi , RequestTaxiList , RequestTaxiDetail , RequestDeliveryList , 
                    ActiveRequsetDelivery , RequsetDeliveryDetail , RequestTruckList ,
                    ActiveRequestTruck , RequestTruckDetail , RequestPickup_truckList ,
                    ActiveRequestPickup_truck , RequestPickup_truckDetail)

app_name = "api"

urlpatterns = [
    path('taxi/all-requests/' , RequestTaxiList.as_view() , name='all-taxi'),
    path('taxi/active-requests/' , ActiveRequsetTaxi.as_view() , name='taxi-active'),
    path('taxi/<int:pk>/' , RequestTaxiDetail.as_view() , name = 'taxi-detail'),
    path('Delivery/all-request/' , RequestDeliveryList.as_view() , name = 'delivery-all'),
    path('Delivery/active-request/' , ActiveRequsetDelivery.as_view() , name = 'delivery-active'),
    path('delivery/<int:pk>/' , RequsetDeliveryDetail.as_view() , name='delivery-detail'),
    path('truck/all-request/' , RequestTruckList.as_view() , name='all-truck'),
    path('truck/active-requests/' , ActiveRequestTruck.as_view() , name = 'truck-active'), 
    path('truck/<int:pk>/' , RequestTruckDetail.as_view(),name = 'truck-detail'),
    path('pickup_truck/all-request/' , RequestPickup_truckList.as_view(),name='all-pickup_truck'),
    path('pickup_truck/active-requests/' , ActiveRequestPickup_truck.as_view(),name = 'pickup_truck-active'),
    path('pickup_truck/<int:pk>/' , RequestPickup_truckDetail.as_view(),name = 'pickup_truck-detail')
]
