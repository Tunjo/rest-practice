from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Bezveze, Storage, Item, ClassesChar, Character
from .serializers import BezvezeSerializer, StorageSerializer, ItemSerializer, StorageDetailSerializer, CharacterSerializer, ClassesCharSerializer, ClassesDetailSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


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
        print(obj_mod.item_description)
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
        serializer.create(validated_data=request.data)
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
        serializer.update(instance=instance, validated_data=request.data)
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


class CharMixin(object):
    def get_object(self):
        id = self.kwargs['id']
        obj_mod = Character.objects.get(id=id)
        return obj_mod


class CharacterListView(ListAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CharacterRetrieveView(CharMixin, RetrieveAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CharacterCreateView(CreateAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()

    def create(self, request, *args, **kwargs):
        data_one = request.data
        serializer = self.get_serializer(data=data_one)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class CharacterUpdateView(UpdateAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
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


class CharacterDeleteView(DestroyAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    lookup_url_kwarg = 'id'


class ClassesListView(ListAPIView):
    serializer_class = ClassesCharSerializer
    # make queryset that filter objects depend on the choice
    # icontains lower and upper case all good
    # & veze 2 queri parametra u browseru
    # ? set query in browser

    def get_queryset(self):
        qs = ClassesChar.objects.all()
        char = self.request.query_params.get('name')
        choice = self.request.query_params.get('choice')
        if char:
            qs = qs.filter(char__name__icontains=char)
        if choice:
            qs = qs.filter(choice=choice)
        return qs


class ClassesRetrieveView(RetrieveAPIView):
    serializer_class = ClassesCharSerializer
    queryset = ClassesChar.objects.all()
    lookup_url_kwarg = 'id'


class ClassesNewView(CreateAPIView):
    serializer_class = ClassesDetailSerializer
    queryset = ClassesChar.objects.all()

    def create(self, request, *args, **kwargs):
        data_one = request.data
        char_id = request.data.get('char')
        try:
            char = Character.objects.get(id=char_id)
        except Item.DoesNotExist:
            char = Character()
            char.save()
        serialize = self.get_serializer(data=data_one)
        serialize.is_valid(raise_exception=True)
        serialize.save(char=char)

        return Response(
            serialize.data,
            status=status.HTTP_201_CREATED
        )


class ClassesUpdateView(UpdateAPIView):
    serializer_class = ClassesDetailSerializer
    queryset = ClassesChar.objects.all()
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


class ClassesDestroyView(DestroyAPIView):
    serializer_class = ClassesDetailSerializer
    queryset = ClassesChar.objects.all()
    lookup_url_kwarg = 'id'


class ItemMixin(object):
    def get_object(self):
        print(self.kwargs)
        id = self.kwargs['id']
        obj_mod = Item.objects.get(id=id)
        return obj_mod


# View set we can have all etc. update, retrive and delete in same view


class ItemViewSet(ItemMixin, viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def retrieve(self, request, *args, **kwargs):

        # self.get_object is method from ItemMixin and it pass it to ItemViewSet

        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
