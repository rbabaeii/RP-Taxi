from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , ListAPIView , CreateAPIView
from .models import Driver_job
from api.models import reqtaxi
from .serializers import Driver_jobserializer , Travel_serializer , Travelcreat_serializer
# Create your views here.

class Travel(ListAPIView):
    queryset = Driver_job.objects.filter(finish=True)
    serializer_class = Driver_jobserializer

class Travel_create(CreateAPIView):
    queryset = reqtaxi.objects.filter(search_for_taxi=True)
    serializer_class = Travelcreat_serializer

class Travel_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Driver_job.objects.all()
    serializer_class = Travel_serializer