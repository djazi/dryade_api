# Generated by Django 3.2.15 on 2022-09-09 15:16

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20220909_1513'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='ordersteps',
            name='start_date_before_end_date',
        ),
        migrations.AddConstraint(
            model_name='ordersteps',
            constraint=models.CheckConstraint(check=models.Q(('order_start_date__lt', django.db.models.expressions.F('order_end_date'))), name='order_start_date_before_order_end_date'),
        ),
    ]
