# Generated by Django 5.0 on 2023-12-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_admin', '0004_alter_categories_name_ru'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category_image')),
            ],
        ),
    ]