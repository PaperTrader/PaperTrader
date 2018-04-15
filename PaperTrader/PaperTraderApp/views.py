from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy

from PaperTraderApp.models import StockModel, AdminStockModel
from PaperTraderApp.StockHandler.StockScraper import StockScraper

# Create your views here.

class ListStockView(ListView):
    model = StockModel
    template_name = 'stock_list.html'

class CreateStockView(CreateView):
    model = StockModel
    template_name = 'create_stock.html'
    fields = ['name', 'symbol']

    def get_success_url(self):
        return reverse('stock-list')

    def form_valid(self, form):
        symbol = form.instance.symbol
        s = StockScraper(symbol)
        form.instance.opening = s.getOpen()
        form.instance.closing = s.getClose()
        form.instance.high = s.getHigh()
        form.instance.low = s.getLow()
        form.instance.volume = s.getVolume()
        return super(CreateStockView, self).form_valid(form)

class DeleteStockView(DeleteView):
    model = StockModel
    template_name = 'stock_confirm_delete.html'
    success_url = reverse_lazy('stock-list')
