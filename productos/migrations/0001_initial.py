# Generated by Django 4.0.2 on 2022-02-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('categoria', models.CharField(max_length=20)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
