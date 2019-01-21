from django.conf.urls import url
from example.appnew import views as bezveze_views

urlpatterns = [
    url(r'^list-bezveze/$', bezveze_views.BezvezeListView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/bezveze/$', bezveze_views.BezvezeRetrieveView.as_view()),
    url(r'^bezveze/add/$', bezveze_views.BezvezeCreateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/bezveze/edit/$', bezveze_views.BezvezeUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/bezveze/delete/$', bezveze_views.BezvezeDestroyView.as_view()),
    url(r'^list-storage/$', bezveze_views.StorageListView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/storage/$', bezveze_views.StorageRetrieveView.as_view()),
    url(r'^item/add/$', bezveze_views.ItemCreateView.as_view()),
    url(r'^storage/add/$', bezveze_views.StorageCreateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/storage/edit',  bezveze_views.StorageUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/item/edit/$', bezveze_views.ItemUpdateView.as_view())
]