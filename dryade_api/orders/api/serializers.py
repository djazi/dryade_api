from rest_framework import serializers

from dryade_api.orders.models import Order
from dryade_api.users.models import User


class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_active"]


class OrderSerializer(serializers.ModelSerializer):
    user = UserOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["order_name", "timestamp", "completed", "updated", "user"]
