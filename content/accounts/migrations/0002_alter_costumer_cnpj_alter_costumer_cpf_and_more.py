# Generated by Django 5.0.1 on 2024-06-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='cnpj',
            field=models.CharField(max_length=34, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='cpf',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='number',
            field=models.CharField(max_length=24, null=True, unique=True),
        ),
    ]