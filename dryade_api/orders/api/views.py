from rest_framework import generics

from dryade_api.orders.api.serializers import OrderSerializer
from dryade_api.orders.models import Order


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
