from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.pagination import PageNumberPagination  
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import CoffeeMachine, CoffeePod
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer

   

class MachineList(ListAPIView):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    seaech_fields = ('product_type', 'water_line_compatible')
    

class PodList(ListAPIView):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeeMachineSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    seaech_fields = ('product_type', 'coffee_flavor', 'pack_size')