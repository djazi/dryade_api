from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.utils import timezone

from dryade_api.users.models import BaseModel, User


class Order(BaseModel):
    order_name = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )

    def clean(self):
        """-- call it by 'obj.full_clean() --"""
        if self.order_name == self.created_by.username:
            raise ValidationError("The order name cannot be the same as the username ")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_name


class OrderSteps(BaseModel):
    order_step = models.CharField(unique=True, max_length=255)
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    order_start_date = models.DateField()
    order_end_date = models.DateField()

    @property
    def has_started(self) -> bool:
        now = timezone.now()

        return self.order_start_date <= now.date()

    @property
    def has_finished(self) -> bool:
        now = timezone.now()

        return self.order_end_date <= now.date()

    def is_within(self, x) -> bool:
        return self.order_start_date <= x <= self.order_end_date

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="order_start_date_before_order_end_date",
                check=Q(order_start_date__lt=F("order_end_date")),
            )
        ]
