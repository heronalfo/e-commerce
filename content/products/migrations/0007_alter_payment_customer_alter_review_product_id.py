# Generated by Django 5.0.1 on 2024-06-26 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_costumer_options_alter_costumer_cep_and_more'),
        ('products', '0006_alter_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='accounts.costumer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='products.product'),
        ),
    ]
