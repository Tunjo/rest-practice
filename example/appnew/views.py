from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Bezveze, Storage, Item
from .serializers import BezvezeSerializer, StorageSerializer, ItemSerializer, StorageDetailSerializer
from rest_framework.response import Response
from rest_framework import status


class BezvezeMixin(object):

    def get_object(self):
        id = self.kwargs['id']
        obj_mod = Bezveze.objects.get(id=id)
        return obj_mod


class BezvezeListView(ListAPIView):
    serializer_class = BezvezeSerializer

    # return list obj

    def get_queryset(self):
        q_operator = Q(name='Tunjo') | Q(last_name='sadasd')
        obj = Bezveze.objects.filter(q_operator)
        return obj


class BezvezeRetrieveView(RetrieveAPIView):
    serializer_class = BezvezeSerializer
    queryset = Bezveze.objects.all()
    lookup_url_kwarg = 'id'


class BezvezeCreateView(CreateAPIView):
    serializer_class = BezvezeSerializer
    queryset = Bezveze.objects.all()

    def create(self, request, *args, **kwargs):
        data_one = request.data
        serializer = self.get_serializer(data=data_one)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class BezvezeUpdateView(BezvezeMixin, UpdateAPIView):
    serializer_class = BezvezeSerializer
    queryset = Bezveze.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # self.get_serializer == item_serializer
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(self.kwargs)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class BezvezeDestroyView(BezvezeMixin, DestroyAPIView):
    serializer_class = BezvezeSerializer
    queryset = Bezveze.objects.all()
    lookup_url_kwarg = 'id'


class StorageMixin(object):

    def get_object(self):
        id = self.kwargs['id']
        obj_mod = Storage.objects.get(item__id=id)
        return obj_mod


class StorageListView(ListAPIView):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()


class StorageRetrieveView(StorageMixin, RetrieveAPIView):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()
    # lookup_url_kwarg = 'item_id'


class ItemCreateView(CreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def create(self, request, *args, **kwargs):
        data_one = request.data
        serializer = self.get_serializer(data=data_one)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class ItemUpdateView(UpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_url_kwarg = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(self.kwargs)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class StorageCreateView(CreateAPIView):
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()

    def create(self, request, *args, **kwargs):
        data_one = request.data
        print(request.data)
        item_id = request.data.get('item')
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            item = Item()
            item.name = 'bla bla'
            item.description = 'sve je top'
            item.price = 33.43
            item.save()
            # item = Item.objects.create(name='bla bla', description='sve je top', price=33.43)
            # .. -- same as instance create and item.save() ----- that is same thing

        serialize = self.get_serializer(data=data_one)
        serialize.is_valid(raise_exception=True)
        serialize.save(item=item)

        return Response(
            serialize.data,
            status=status.HTTP_201_CREATED
        )


class StorageUpdateView(UpdateAPIView):
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()
    lookup_url_kwarg = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(self.kwargs)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

