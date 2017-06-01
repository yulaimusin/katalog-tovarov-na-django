from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<category_slug>[\w-]+)/(?P<product_id>\d+)_(?P<product_slug>[\w-]+)/$', views.product_details,
        name='details'),
    url(r'^(?P<category_slug>[\w-]+)/$', views.product_list, name='list'),
    url(r'', views.product_list_homepage, name='homepage'),
]
