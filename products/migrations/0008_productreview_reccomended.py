# Generated by Django 3.2 on 2022-01-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220126_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='reccomended',
            field=models.BooleanField(default=True),
        ),
    ]
