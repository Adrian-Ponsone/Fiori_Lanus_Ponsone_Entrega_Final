# Generated by Django 4.1.3 on 2022-11-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userextension_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextension',
            name='user_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]