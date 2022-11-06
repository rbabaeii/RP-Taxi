from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView , CreateAPIView
from .models import Driver_job
from .serializers import Driver_jobserializer , Travel_serializer , Travelcreat_serializer
from .permissions import DriverPermission , OwnerOrStaff

class Travel(ListAPIView):
    queryset = Driver_job.objects.filter(finish=True)
    serializer_class = Driver_jobserializer
    permission_classes = (DriverPermission , )

class Travel_create(CreateAPIView):
    def get_queryset(self):
        return  Driver_job.objects.filter(body__search_for_taxi=True)
    serializer_class = Travelcreat_serializer
    permission_classes = (DriverPermission , )

class Travel_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Driver_job.objects.all()
    serializer_class = Travel_serializer
    permission_classes = (OwnerOrStaff , )