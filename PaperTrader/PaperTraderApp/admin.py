from django.contrib import admin
from PaperTraderApp.models import StockModel, AdminStockModel

admin.site.register(StockModel)
admin.site.register(AdminStockModel)

