from django.urls import path
from .views import ReadingOrdersWithListProducts

urlpatterns = [
    path('list_products/<int:user_id>/<int:days>/', ReadingOrdersWithListProducts.as_view(), 
         name='reading_orders_with_list_products'),
]

# http://127.0.0.1:8000/homework_3_app/list_products/1/7
