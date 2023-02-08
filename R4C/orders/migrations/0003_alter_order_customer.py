# Generated by Django 4.1.5 on 2023-01-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('orders', '0002_remove_order_robot_serial_order_robot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(help_text='Order customer', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customers.customer', verbose_name='customer'),
        ),
    ]
