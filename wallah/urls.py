from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeadListCreate.as_view() ),
    path('products/', views.ProductListCreate.as_view() ),
    path('orders/', views.OrderListCreate.as_view() ),
]

