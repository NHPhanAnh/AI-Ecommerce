from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager_home, name='manager_home'),
    path('add/', views.add_item, name='add_item'),
    path('product/<int:item_id>/', views.product_detail_edit, name='product_detail_edit'),
]
