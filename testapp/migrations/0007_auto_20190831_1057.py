# Generated by Django 2.2.3 on 2019-08-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20190831_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatting',
            name='Created_Date',
            field=models.DateTimeField(),
        ),
    ]
