# Generated by Django 5.0.1 on 2024-07-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_orderitem_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='products.orderitem'),
        ),
    ]
