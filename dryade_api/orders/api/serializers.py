from rest_framework import serializers

from dryade_api.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_name", "timestamp", "completed", "updated", "user"]
