from django.conf.urls import url
from example.appnew import views as bezveze_views

urlpatterns = [
    url(r'^list-bezveze/$',
        bezveze_views.BezvezeListView.as_view()
        ),
    url(r'^list-bezvz/$',
        bezveze_views.BzvzNewListView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/bezveze/$',
        bezveze_views.BezvezeRetrieveView.as_view()
        ),
    url(r'^bezveze/add/$',
        bezveze_views.BezvezeCreateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/bezveze/edit/$',
        bezveze_views.BezvezeUpdateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/bezveze/delete/$',
        bezveze_views.BezvezeDestroyView.as_view()
        ),
    url(r'^list-storage/$',
        bezveze_views.StorageListView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/storage/$',
        bezveze_views.StorageRetrieveView.as_view()
        ),
    url(r'^item/add/$',
        bezveze_views.ItemCreateView.as_view()
        ),
    url(r'^item-viewset/(?P<id>[\d\w-]+)/$',
        bezveze_views.ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
        ),
    url(r'^storage/add/$',
        bezveze_views.StorageCreateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/storage/edit',
        bezveze_views.StorageUpdateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/item/edit/$',
        bezveze_views.ItemUpdateView.as_view()
        ),
    url(r'^list-char/$',
        bezveze_views.CharacterListView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/char/$',
        bezveze_views.CharacterRetrieveView.as_view()
        ),
    url(r'^char/add/$',
        bezveze_views.CharacterCreateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/char/update/$',
        bezveze_views.CharacterUpdateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/char/delete/$',
        bezveze_views.CharacterDeleteView.as_view()
        ),
    url(r'^list-class/$',
        bezveze_views.ClassesListView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/class/$',
        bezveze_views.ClassesRetrieveView.as_view()
        ),
    url(r'^class/add/$',
        bezveze_views.ClassesNewView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/class/update/$',
        bezveze_views.ClassesUpdateView.as_view()
        ),
    url(r'^(?P<id>[\d\w-]+)/class/delete/$',
        bezveze_views.ClassesDestroyView.as_view()
        ),
    url(r'^list-blackberry/$',
        bezveze_views.BVineListView.as_view()
        ),
    url(r'^blackberry/add/$',
        bezveze_views.BVineCreateView.as_view()
        ),
    url(r'^order/add/$',
        bezveze_views.OrderCreateView.as_view()
        ),
    url(r'^list-costumer/$',
        bezveze_views.CostumerListView.as_view()
        ),
    url(r'^costumer/add/$',
        bezveze_views.CostumerCreateView.as_view()
        ),
]