# Generated by Django 2.1.7 on 2019-03-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
