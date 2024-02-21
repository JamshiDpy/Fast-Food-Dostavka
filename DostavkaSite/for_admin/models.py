from django.db import models
from django_resized import ResizedImageField
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Categories(models.Model):
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    child = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_category')
    image = ResizedImageField(upload_to="category_images", size=[640, 640])

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"


class CategoryImage(models.Model):
    image = ResizedImageField(upload_to='category_main', size=[640, 640])


class Products(models.Model):
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = ResizedImageField(upload_to='product_images', size=[640, 640])
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name_uz


@receiver(pre_save, sender=Categories)
def category_name(sender, instance, **kwargs):
    instance.name_uz = str(instance.name_uz).capitalize()
    instance.name_ru = str(instance.name_ru).capitalize()


@receiver(pre_save, sender=CategoryImage)
def delete_old_image(sender, instance, **kwargs):
    obj = CategoryImage.objects.all()
    if obj.count() > 0:
        obj[0].delete()


@receiver(pre_save, sender=Products)
def product_name(sender, instance, **kwargs):
    instance.name_uz = str(instance.name_uz).capitalize()
    instance.name_ru = str(instance.name_ru).capitalize()
