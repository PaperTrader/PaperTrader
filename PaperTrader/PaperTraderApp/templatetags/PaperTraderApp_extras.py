from django import template
from PaperTraderApp.models import StockModel

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    s = StockModel.objects.get(symbol=value)
    return arg*s.opening

