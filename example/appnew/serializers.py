from rest_framework import serializers
from .models import (
    Bezveze,
    Storage,
    Item,
    Character,
    ClassesChar,
    Order,
    Costumer,
    BlackberryVine
)



class BezvezeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bezveze
        fields = (
            'name',
            'sur_name',
            'last_name',
            'id'
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

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        price = validated_data.get('price')
        item = Item()
        item.name = name
        item.description = description
        item.price = price
        item.save()
        return item

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.price = validated_data.get('price')
        instance.save()
        return instance


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            # item serializer
            'item',
            'quantity',
            'item_name',
            'i_price',
            'item_description'
        )
    # item is == Item and we can get all values objects from Item model,
    # in this case field item is == ItemSerializer and from him we can get all fields in Item model
    item = ItemSerializer()
    item_name = serializers.CharField(read_only=True, source='item.name')
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


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', )


class ClassesCharSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassesChar
        fields = (
            'char',
            'choice'
        )
    char = CharacterSerializer()
    choice = serializers.SerializerMethodField()

    def get_choice(self, classes):
        return classes.get_choice_display()


class ClassesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassesChar
        fields = (
            'char',
            'choice'
        )


class BVineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackberryVine
        fields = (
            'vine_choice',
        )

    vine_choice = serializers.SerializerMethodField()

    def get_vine_choice(self, blackberry):
        return blackberry.get_vine_choice_display()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order', )

    order = serializers.SerializerMethodField()

    def get_order(self, ord):
        return ord.get_order_display()


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = (
            'name',
            'address',
            'comment',
            'ord',
            'product',
            'order',
            'prod'
        )

    #ord = serializers.CharField(source='ord.pk', write_only=True)
    #order = OrderSerializer(read_only=True)
    order = serializers.SerializerMethodField()
    #product = serializers.CharField(source='product.pk', write_only=True)
    #prod = BVineSerializer(read_only=True)
    prod = serializers.SerializerMethodField()

    def get_order(self, obj):
        return OrderSerializer(obj.ord).data

    def get_prod(self, obj):
        return BVineSerializer(obj.product).data


class CostumerSerializerDisplay(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = (
            'name',
            'address',
            'comment',
            'ord',
            'product'
        )

    ord = OrderSerializer()
    product = BVineSerializer()




