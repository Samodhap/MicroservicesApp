from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.view_products, name="products"),
    path('products/<str:pk>/', views.view_detailed_product, name="product"),
    path('add/',views.add_products,name="add-products"),
    path('update/<str:pk>/',views.update_product,name="update-product"),
    path('delete/<str:pk>/',views.delete_product,name="delete-product")
]