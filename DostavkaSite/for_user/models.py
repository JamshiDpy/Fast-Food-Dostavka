from django.db.models import (Model, CharField, BooleanField, BigIntegerField, IntegerField, ForeignKey, CASCADE,
                              ManyToManyField, DateTimeField, FloatField)

from for_admin import models
from django.utils import timezone


class BotUsers(Model):
    telegram_id = BigIntegerField()
    phone_number = CharField(max_length=13)
    telegram_username = CharField(max_length=150, null=True, blank=True)
    language = CharField(max_length=4)

    def __str__(self):
        return self.phone_number


class Basket(Model):
    user = ForeignKey(BotUsers, on_delete=CASCADE)
    product = ForeignKey(models.Products, on_delete=CASCADE)
    quantity = IntegerField()
    ordered = BooleanField(default=False)

    @property
    def total_price(self):
        # try:
        #     sum_ = int(self.product.price) * self.quantity
        # except:
        #     sum_ = self.product.price * self.quantity
        sum_ = self.product.price * self.quantity
        return '{:0,.0f} so\'m'.format(sum_)


class Order(Model):
    user = ForeignKey(BotUsers, on_delete=CASCADE)
    orders = ManyToManyField(Basket)
    latitude = CharField(max_length=100, null=True, blank=True)
    longitude = CharField(max_length=100, null=True, blank=True)
    date = DateTimeField(auto_now_add=timezone.now())
    delivered = BooleanField(default=False)

    @property
    def total_price(self):
        price = 0.0
        for product in self.orders:
            price += product.price
        return price
