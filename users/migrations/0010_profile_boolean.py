# Generated by Django 3.2 on 2021-05-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='boolean',
            field=models.BooleanField(default=True),
        ),
    ]
