# Generated by Django 5.0.1 on 2024-07-13 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
    ]