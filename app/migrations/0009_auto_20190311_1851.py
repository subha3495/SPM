# Generated by Django 2.1.7 on 2019-03-11 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190311_1819'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Add_Agent',
        ),
        migrations.DeleteModel(
            name='add_company',
        ),
        migrations.DeleteModel(
            name='companyreg',
        ),
        migrations.DeleteModel(
            name='Customer_Registration',
        ),
    ]