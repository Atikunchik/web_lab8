from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path(
        "products",
        views.list_products,
        name="product-list"
    ),
    path(
        "product/<int:product_id>",
        views.get_product,
        name="product-get"
    ),
    path(
        "categories",
        views.list_categories,
        name="category-list"
    ),
    path(
        "category/<int:catefory_id>",
        views.get_category,
        name="category-get"
    ),
]