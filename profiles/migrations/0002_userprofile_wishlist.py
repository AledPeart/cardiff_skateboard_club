# Generated by Django 3.2 on 2022-01-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_productreview'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
