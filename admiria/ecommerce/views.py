from django.shortcuts import render

# Create your views here.
# Ecommerce-Pages
def ecommerce_product_list(request):
    greeting = {}
    greeting['title'] = "Product List"
    greeting['path'] = "Ecommerce"
    return render(request,'pages/Extra/ecommerce/ecommerce-product-list.html',greeting)
def ecommerce_product_grid(request):
    greeting = {}
    greeting['title'] = "Product Grid"
    greeting['path'] = "Ecommerce"
    return render(request,'pages/Extra/ecommerce/ecommerce-product-grid.html',greeting)
def ecommerce_order_history(request):
    greeting = {}
    greeting['title'] = "Order History"
    greeting['path'] = "Ecommerce"
    return render(request,'pages/Extra/ecommerce/ecommerce-order-history.html',greeting)
def ecommerce_customers(request):
    greeting = {}
    greeting['title'] = "Customers"
    greeting['path'] = "Ecommerce"
    return render(request,'pages/Extra/ecommerce/ecommerce-customers.html',greeting)
def ecommerce_product_edit(request):
    greeting = {}
    greeting['title'] = "Product Edit"
    greeting['path'] = "Ecommerce"
    return render(request,'pages/Extra/ecommerce/ecommerce-product-edit.html',greeting)