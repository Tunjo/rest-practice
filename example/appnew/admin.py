from django.contrib import admin
from .models import Bezveze, Item, Storage, ClassesChar, Character, BlackberryVine, Order, Costumer


class AdminStorage(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price')

    def price(self, storage):
        return storage.item.price


class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


class AdminBezveze(admin.ModelAdmin):
    list_display = ('name', 'sur_name', 'last_name')


class AdminClassesChar(admin.ModelAdmin):
    list_display = ('char', 'choice')


class AdminCostumer(admin.ModelAdmin):
    list_display = ('product', 'ord', 'name', 'address', 'comment')


admin.site.register(Bezveze, AdminBezveze)
admin.site.register(Item, AdminItem)
admin.site.register(Storage, AdminStorage)
admin.site.register(ClassesChar, AdminClassesChar)
admin.site.register(Character)
admin.site.register(BlackberryVine)
admin.site.register(Order)
admin.site.register(Costumer, AdminCostumer)
