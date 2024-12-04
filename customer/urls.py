from django.urls import path
from . import views
urlpatterns = [
    path('customer_list/',views.customer_list,name='customer_list'),
    path('customer/<int:id>/',views.customer_detail,name='customer_detail'),
    path('customer/add/',views.customer_add,name='customer_add'),
    path('customer/<int:id>/edit/',views.customer_edit,name='customer_edit'),
    path('customer/<int:id>/delete/',views.customer_delete,name='customer_delete'),
    path('<int:customer_id>/orders/', views.order_list, name='order_list'),
    path('<int:customer_id>/orders/add/', views.order_form, name='order_form'),
    path('orders/<int:order_id>/edit/', views.edit_order, name='edit_order'),
    path('', views.dashboard, name='dashboard'),
    ]