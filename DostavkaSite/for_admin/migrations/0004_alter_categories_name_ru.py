# Generated by Django 5.0 on 2023-12-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_admin', '0003_rename_name_categories_name_uz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name_ru',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
