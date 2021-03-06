# Generated by Django 4.0.5 on 2022-06-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bobina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=30)),
                ('cliente', models.CharField(max_length=20)),
                ('buque', models.CharField(max_length=20)),
                ('criticidad', models.CharField(max_length=10)),
                ('peso', models.IntegerField()),
                ('ancho', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('transporte', models.CharField(max_length=60)),
                ('contacto', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tractor', models.CharField(max_length=7)),
                ('semi', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=15)),
            ],
        ),
    ]
