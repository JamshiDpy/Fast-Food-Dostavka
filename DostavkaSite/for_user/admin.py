from django.contrib import admin

from .models import BotUsers, Basket, Order


# Register your models here.

class BasketModelAdmin(admin.ModelAdmin):
    # readonly_fields = ['user', 'product', 'quantity', 'total_price']
    list_display = ['user', 'product']
    # fieldsets = ['total_price']


admin.site.register(BotUsers)
admin.site.register(Basket, BasketModelAdmin)
admin.site.register(Order)
