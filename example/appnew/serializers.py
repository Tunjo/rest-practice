from rest_framework import serializers
from .models import Bezveze, Storage, Item


class BezvezeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bezveze
        fields = (
            'name',
            'sur_name',
            'last_name'
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'name',
            'description',
            'price',
            'id'
        )


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            # item serializer
            'item',
            'quantity',
            'item_price',
            'i_price'
        )
    # item is == Item and we can get all values objects from Item model,
    # in this case field item is == ItemSerializer and from him we can get all fields in Item model
    item = ItemSerializer()
    item_price = serializers.CharField(read_only=True, source='item.name')
    # we can get items from Item model
    i_price = serializers.SerializerMethodField()
    # i_price is method call with serializer method field, we write method

    def get_i_price(self, storage):
        return storage.item.price



class StorageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            'item',
            'quantity'
        )
    # item = ItemSerializer()





