# Generated by Django 4.0.2 on 2022-02-26 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_producto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
    ]