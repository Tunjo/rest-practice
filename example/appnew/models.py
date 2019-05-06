from django.db import models


class Bezveze(models.Model):
    name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True)

    def __str__(self):
        return self.name


class Storage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def item_description(self):
        return self.item.description


class Character(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClassesChar(models.Model):

    CLASS_LIST = (
        (1, 'Warrior'),
        (2, 'Mage'),
        (3, 'Priest')
    )

    char = models.ForeignKey(Character, on_delete=models.CASCADE)
    choice = models.PositiveSmallIntegerField(choices=CLASS_LIST)


class BlackberryVine(models.Model):

    VINE_CHOICE = (
        (1, 'Blackberry075'),
        (2, 'Blackberry050'),
        (3, 'Blackberry025')
    )

    vine_choice = models.PositiveSmallIntegerField(choices=VINE_CHOICE)

    def __str__(self):
        return self.get_vine_choice_display()


class Order(models.Model):

    ORDER_CHOICE = (
        (1, 'Palette'),
        (2, 'Box'),
        (3, 'Individual')
    )

    order = models.PositiveSmallIntegerField(choices=ORDER_CHOICE)

    def __str__(self):
        return self.get_order_display()


class Costumer(models.Model):
    product = models.ForeignKey(BlackberryVine, on_delete=models.CASCADE)
    ord = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    comment = models.TextField(blank=True)
