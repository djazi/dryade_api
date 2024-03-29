from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dryade_api.orders.api import views

app_name = "orders"


urlpatterns = [
    # CRUD API for orders
    path("list/", views.OrderList.as_view()),
    path("create/", views.OrderCreate.as_view()),
    path("udate/<int:pk>/", views.OrderUpdate.as_view()),
    path("retreive/<int:pk>/", views.OrderRetrieve.as_view()),
    path("destroy/<int:pk>/", views.OrderDestroy.as_view()),
    # CRUD APIS for orders steps
    path("steps/list/", views.OrderStepsList.as_view()),
    # Bulk CRUD APIS for orders
    path("generate_link", views.generate_link, name="generate_link"),
    path("one_time_link/<str:access_code>", views.one_time_link, name="one_time_link"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
