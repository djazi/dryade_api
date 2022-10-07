from django.contrib import admin

from dryade_api.orders.models import Order, OrderSteps


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_name",
        "created_by",
        "completed",
        "created_at",
        "updated_at",
        "is_deleted",
    )


class OrderStepsAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "order_step",
        "order_start_date",
        "order_end_date",
        "created_at",
        "updated_at",
        "is_deleted",
        "is_deleted",
    )


admin.site.register(OrderSteps, OrderStepsAdmin)
admin.site.register(Order, OrderAdmin)
