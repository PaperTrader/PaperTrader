# Generated by Django 2.0.2 on 2018-04-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaperTraderApp', '0008_auto_20180416_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmodel',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='symbol',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
