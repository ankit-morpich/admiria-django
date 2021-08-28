from django.urls import path, include
from . import views

urlpatterns = [
   # Ecommerce-Pages
    path('ecommerce-product-list', views.ecommerce_product_list, name="ecommerce-product-list"),
    path('ecommerce-product-grid', views.ecommerce_product_grid, name="ecommerce-product-grid"),
    path('ecommerce-order-history', views.ecommerce_order_history, name="ecommerce-order-history"),
    path('ecommerce-customers', views.ecommerce_customers, name="ecommerce-customers"),
    path('ecommerce-product-edit', views.ecommerce_product_edit, name="ecommerce-product-edit"),  

]