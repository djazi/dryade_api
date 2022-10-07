import random
import string

from django.http import HttpResponse
from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from dryade_api.orders.api import serializers
from dryade_api.orders.models import OneTimeLinkModel, Order, OrderSteps


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


class OrderStepsList(generics.ListAPIView):

    queryset = OrderSteps.objects.all().filter(is_deleted=False)
    serializer_class = serializers.OrderStepListSerializer


# generates the string of the one time URL
def randomString(stringLength=20):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(stringLength))


# generates the link itself
def generate_link(request):
    the_string = randomString(stringLength=20)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return HttpResponse(
        f'<a href="/orders/one_time_link/{the_string}">{request.build_absolute_uri()}{the_string}</a>'
    )


# handles the link request
def one_time_link(request, access_code=0):

    obj = OneTimeLinkModel.objects.filter(one_time_code=access_code)
    if access_code == 0:
        return HttpResponse("Test link")
    # check if object exists and time difference is less than 3 minutes
    elif obj.exists() and (timezone.now() - obj[0].expiry_time).total_seconds() < 5:
        # remove the line below if you do not want the link to self destruct after it has been used
        OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
        return HttpResponse(
            "Hey, your linked worked. Make sure to download as it won't work again."
        )

    elif not obj.exists():
        return HttpResponse("Bad link.")
    else:
        return HttpResponse("expired link.")
