# Generated by Django 5.0.1 on 2024-07-07 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_costumer_options_alter_costumer_cep_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costumer',
            options={'verbose_name': 'costumer', 'verbose_name_plural': 'costumers'},
        ),
    ]
