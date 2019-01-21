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


