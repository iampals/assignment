from rest_framework import generics

from .models import Dashboard
from .serializers import DashboardSerializer

class ListDashboard(generics.ListCreateAPIView):
    queryset = Dashboard.objects
   # import pdb;pdb.set_trace()
    serializer_class = DashboardSerializer

    def perform_create(self,serializer):
        serializer.save()


class DetailDashboard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
