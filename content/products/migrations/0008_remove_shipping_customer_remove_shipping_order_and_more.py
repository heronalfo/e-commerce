# Generated by Django 5.0.1 on 2024-07-13 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_image_shipping_sent_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='order',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]