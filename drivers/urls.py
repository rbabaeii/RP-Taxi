from django.urls import path,include
from .views import Travel , Travel_Detail , Travel_create

app_name = "drivers"

urlpatterns = [
    path('',Travel.as_view()),
    path('<int:pk>/' , Travel_Detail.as_view()),
    path('create/' , Travel_create.as_view()),
]
