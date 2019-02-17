from django.conf.urls import url
from store.views import Home, Products, SingleProduct, EditProduct
from . import views

urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^products$', Products.as_view()),
    url(r'^products/(?P<id>\d+)$', SingleProduct.as_view()),
    url(r'^products/(?P<id>\d+)/change$', EditProduct.as_view()),
    url(r'^sortbrand', views.sortByBrand),
    url(r'^sortname', views.sortByName),
    url(r'^sortprice', views.sortByPrice),
    url(r'^sortcreated', views.sortByCreated),
    url(r'^sortupdated', views.sortByUpdated)
]