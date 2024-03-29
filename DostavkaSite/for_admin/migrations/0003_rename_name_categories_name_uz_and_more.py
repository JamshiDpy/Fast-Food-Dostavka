# Generated by Django 5.0 on 2023-12-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_admin', '0002_products_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='name',
            new_name='name_uz',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='name_ru',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.AddField(
            model_name='categories',
            name='name_ru',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='name_uz',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
