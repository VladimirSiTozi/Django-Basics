from django import template
from django.db.models import Sum

register = template.Library()


@register.filter
def total_price(car_set):
    return car_set.aggregate(Sum('price'))['price__sum'] or 0
