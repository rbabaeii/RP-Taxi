from django.urls import path,include
from .views import Travel , Travel_Detail , Travel_create

app_name = "drivers"

urlpatterns = [
    path('travel-list/',Travel.as_view()),
    path('travel-detail/<int:pk>/' , Travel_Detail.as_view()),
    path('travel/create/' , Travel_create.as_view()),
]
