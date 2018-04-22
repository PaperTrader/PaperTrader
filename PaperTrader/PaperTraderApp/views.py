from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.forms import ModelForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from PaperTraderApp.models import StockModel, AdminStockModel, PortfolioModel
from PaperTraderApp.StockHandler.StockScraper import StockScraper
from PaperTraderApp.StockHandler.StockFactory import StockFactory

from django.contrib.auth import authenticate, login

# Create your views here.

class ListStockView(ListView):
    model = StockModel
    template_name = 'stock_list.html'

def update_stock_info(something):
    s = StockFactory()
    s.updateAll()

    return HttpResponseRedirect("/")

def add_to_portfolio(request, pk):
    model = PortfolioModel
    stock = StockModel.objects.get(pk=pk)
    stockFactory = StockFactory()
    stockObj = stockFactory.getStockObject(stock.symbol)
    obj = model.objects.get_or_create(pk=request.user.id)[0]
    current_stocks = obj.get_stocks()
    current_stocks[stockObj.getSymbol()] = current_stocks[stockObj.getSymbol()] + 1 if stockObj.getSymbol() in current_stocks.keys() else 1
    obj.set_stocks(current_stocks)
    obj.save()
    return HttpResponseRedirect("/")
    #return render_to_response("portfolio.html", {'stocks' : stock})
    
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

def delete_from_portfolio(request, key):
    portfolio = PortfolioModel.objects.get_or_create(pk=request.user.id)[0]
    current_stocks = portfolio.get_stocks()
    del current_stocks[key]
    portfolio.set_stocks(current_stocks)
    portfolio.save()
    stocks = portfolio.get_stocks()
    return render(request, 'portfolio.html', {'portfolio': portfolio,'stocks': stocks,  'user' : request.user})

def getPortfolio(request):
    print(request.user)
    portfolio = PortfolioModel.objects.get_or_create(pk=request.user.id)[0]
    stocks = portfolio.get_stocks()

    return render(request, 'portfolio.html', {'portfolio': portfolio,'stocks': stocks,  'user' : request.user})

def signup(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect("/")
    #     return HttpResponseRedirect('/signup')
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'signup.html', {'form': form})





