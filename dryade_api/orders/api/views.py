from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from dryade_api.orders.api import serializers
from dryade_api.orders.models import Order


class OrderList(generics.ListAPIView):

    queryset = Order.objects.all().filter(is_deleted=False)
    serializer_class = serializers.OrderListSerializer


class OrderCreate(generics.CreateAPIView):

    queryset = Order.objects.all()
    serializer_class = serializers.OrderCretaeSerializer

    def perform_create(self, serializer):
        "override perform create"
        serializer.save(created_by=self.request.user)


class OrderRetrieve(generics.RetrieveAPIView):

    queryset = Order.objects.all().filter(is_deleted=False)
    serializer_class = serializers.OrderRetrieveSerializer


class OrderUpdate(generics.UpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = serializers.OrderUpdateSerializer


class OrderDestroy(generics.DestroyAPIView):

    queryset = Order.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            status = HTTP_404_NOT_FOUND
        else:
            instance.is_deleted = True
            instance.save()
            status = HTTP_204_NO_CONTENT
        return Response(status=status)
