# Generated by Django 4.1.3 on 2022-11-09 09:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]