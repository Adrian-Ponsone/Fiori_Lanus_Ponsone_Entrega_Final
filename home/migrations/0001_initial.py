# Generated by Django 4.1.3 on 2022-11-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_fabricant', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=20)),
                ('car_type', models.CharField(max_length=20)),
                ('car_color', models.CharField(max_length=20)),
                ('car_year', models.IntegerField()),
                ('fabrication_date', models.DateField()),
            ],
        ),
    ]
