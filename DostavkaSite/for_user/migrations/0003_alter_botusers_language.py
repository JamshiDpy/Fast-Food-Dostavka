# Generated by Django 5.0 on 2023-12-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_user', '0002_basket_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botusers',
            name='language',
            field=models.CharField(max_length=4),
        ),
    ]