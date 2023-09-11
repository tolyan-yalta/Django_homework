from django.shortcuts import render
from homework_2_app.models import User, Order
from datetime import timedelta, datetime
import datetime
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse



class ReadingOrdersWithListProducts(View):
    def get(self, request, user_id, days):
        user = User.objects.get(pk=user_id)
        start_date = datetime.date.today() - timedelta(days=days)
        queryset = Order.objects.select_related('product_id').filter(user_id=
                    user_id).filter(making_order__gte=start_date).order_by('making_order')
        products = []
        for order in queryset:
            products.append({"name": order.product_id.name,
                            "price": order.product_id.price,
                            "quantity": order.product_id.quantity,
                            "date": order.making_order,
                            })
        context = {"days": days, "user": user, "products": products}
        return render(request, "homework_3_app/list_products.html", context)
