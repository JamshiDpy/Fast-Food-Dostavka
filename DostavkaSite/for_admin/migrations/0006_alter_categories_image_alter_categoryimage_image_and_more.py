# Generated by Django 5.0 on 2023-12-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_admin', '0005_categoryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(height_field=640, upload_to='category_images', width_field=640),
        ),
        migrations.AlterField(
            model_name='categoryimage',
            name='image',
            field=models.ImageField(height_field=640, upload_to='category_image', width_field=640),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(height_field=640, upload_to='product_images', width_field=640),
        ),
    ]
