from django.contrib import admin

from dryade_api.orders.models import Order


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


admin.site.register(Order, OrderAdmin)
