from django.urls import path,include
from .views import (ActiveRequsetTaxi,RequestTaxiList,RequestTaxiDetail, RequestDeliveryList , 
                    ActiveRequsetDelivery , RequsetDeliveryDetail)

app_name = "api"

urlpatterns = [
    path('taxi/all-requests/' , RequestTaxiList.as_view(), name='all-taxi'),
    path('taxi/active-requests/', ActiveRequsetTaxi.as_view(), name='taxi-active'),
    path('taxi/<int:pk>/' , RequestTaxiDetail.as_view(), name = 'taxi-detail'),
    path('Delivery/all-request/' , RequestDeliveryList.as_view() , name = 'delivery-all'),
    path('Delivery/active-request/' , ActiveRequsetDelivery.as_view() , name = 'delivery-active'),
    path('delivery/<int:pk>/' , RequsetDeliveryDetail.as_view() , name='delivery-detail')
]
