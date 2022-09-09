from django.core.exceptions import ValidationError
from django.db import models

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
