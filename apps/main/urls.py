from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/new$', views.add_show),
    url(r'^shows$', views.all_shows),
    url(r'^create$', views.create_show),
    url(r'^edit/(?P<showId>\d+)$', views.edit),
    url(r'^update/(?P<showId>\d+)$', views.update),
    url(r'^shows/(?P<showId>\d+)$', views.show_id),
    url(r'^delete/(?P<showId>\d+)$', views.delete),
]