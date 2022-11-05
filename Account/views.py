from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .permissions import Is_StaffOrAdminReadonly , IsSuperUser
from django.views import View 
from django.shortcuts import render
from .models import User
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
