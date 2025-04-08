from django.urls import path
from .views import store_list, view_product

urlpatterns = [
    path('', store_list, name='store_list'),
    path('view_product/', view_product, name='view_product'),
]
