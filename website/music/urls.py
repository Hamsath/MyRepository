from django.conf.urls import url
from . import views

app_name='music'
urlpatterns = [
    #  /music/
    url(r'^$',views.IndexView.as_view(), name = "index"),

    # /register/
    url(r'^register/$',views.UserFormView.as_view(), name = "register"),

    # /music/342
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name ='details'),

    #/music/album/add

    url(r'^album/add/$', views.CreateAlbum.as_view(), name ='album-add'),

    #/music/album/2

    url(r'^album/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name ='album-update'),

    #/music/album/2/delete

    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name ='album-delete'),

]
