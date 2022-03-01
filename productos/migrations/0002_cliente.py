# Generated by Django 4.0.2 on 2022-02-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('condicion_iva', models.CharField(max_length=50)),
            ],
        ),
    ]
