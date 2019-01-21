from django.contrib import admin
from .models import Bezveze, Item, Storage


class AdminStorage(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price')

    def price(self, storage):
        return storage.item.price


class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


class AdminBezveze(admin.ModelAdmin):
    list_display = ('name', 'sur_name', 'last_name')


admin.site.register(Bezveze, AdminBezveze)
admin.site.register(Item, AdminItem)
admin.site.register(Storage, AdminStorage)
