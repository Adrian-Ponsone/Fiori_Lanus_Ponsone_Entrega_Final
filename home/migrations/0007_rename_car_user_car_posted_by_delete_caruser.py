# Generated by Django 4.1.3 on 2022-11-10 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_car_car_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_user',
            new_name='posted_by',
        ),
        migrations.DeleteModel(
            name='CarUser',
        ),
    ]
