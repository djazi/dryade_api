from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dryade_api.orders.api import views

app_name = "orders"


urlpatterns = [
    path("list/", views.OrderList.as_view()),
    path("detail/<int:pk>/", views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
