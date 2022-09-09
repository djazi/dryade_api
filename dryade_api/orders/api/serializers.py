from rest_framework import serializers

from dryade_api.orders.models import Order, OrderSteps
from dryade_api.users.models import User


class UserSerializerOrders(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class OrderListSerializer(serializers.ModelSerializer):
    created_by = UserSerializerOrders(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "order_name",
            "timestamp",
            "completed",
            "updated_at",
            "created_by",
            "is_deleted",
            "created_at",
        ]


class OrderCretaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "order_name",
            "timestamp",
            "completed",
            "created_by",
            "is_deleted",
        ]


class OrderRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserSerializerOrders(read_only=True)

    class Meta:
        model = Order
        fields = [
            "order_name",
            "timestamp",
            "completed",
            "created_by",
            "is_deleted",
            "created_at",
            "updated_at",
        ]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "order_name",
            "timestamp",
            "completed",
            "is_deleted",
            "created_at",
            "updated_at",
        ]


class OrderListSerializer2(serializers.ModelSerializer):
    created_by = UserSerializerOrders(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "created_by",
            "order_name",
            "is_deleted",
        ]


class OrderStepListSerializer(serializers.ModelSerializer):
    order = OrderListSerializer2(read_only=True)

    class Meta:
        model = OrderSteps
        fields = [
            "order_step",
            "order",
            "order_start_date",
            "order_end_date",
            "created_at",
            "updated_at",
            "is_deleted",
        ]
