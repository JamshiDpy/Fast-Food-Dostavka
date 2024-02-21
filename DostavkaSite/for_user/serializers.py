from rest_framework import serializers

from . import models
from for_admin import models as admin_model


class BotUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BotUsers
        fields = ["id", "telegram_id", "phone_number", "telegram_username", "language"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_model.Categories
        fields = ['id', 'name_uz', 'name_ru', 'child', 'image']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = admin_model.Products
        fields = ['id', 'name_uz', 'name_ru', 'category', 'description_uz', 'description_ru', 'image', 'price']


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_model.CategoryImage
        fields = ['image']


class BasketSerializer(serializers.ModelSerializer):
    user = BotUsersSerializer()
    product = ProductSerializer()

    class Meta:
        model = models.Basket
        fields = ['id', 'user', "product", 'quantity', 'total_price', 'ordered']

    # def to_representation(self, instance):
    #     repr = super(BasketSerializer, self).to_representation(instance)
    #     repr['user'] = BasketSerializer(instance.user).data
    #     return repr


class OrderSerializer(serializers.ModelSerializer):
    user = BotUsersSerializer()

    class Meta:
        model = models.Order
        fields = ['id', 'user', 'orders', 'latitude', 'longitude', "date"]

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation['orders'] = BasketSerializer(instance.orders, many=True).data
        return representation
