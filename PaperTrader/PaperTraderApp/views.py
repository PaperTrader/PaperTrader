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

    portfolio = model.objects.get_or_create(pk=request.user.id)[0]

    portfolio.buy(stockObj, 1)

    '''current_stocks = portfolio.get_stocks()
                current_stocks[stockObj.getSymbol()] = current_stocks[stockObj.getSymbol()] + 1 if stockObj.getSymbol() in current_stocks.keys() else 1
                portfolio.set_stocks(current_stocks)
                portfolio.save()'''

    return HttpResponseRedirect("/portfolio")
    #return render_to_response("portfolio.html", {'stocks' : stock})

def add_cash(request):
    print("HEREEEE")
    return render(request, 'add_cash.html')

def add_cash_response(request):

    #can refactor guard clauses later
    if request.method == 'POST':
        if request.POST.get('amount', False):
            amount = int(request.POST['amount'])      

            model = PortfolioModel
            portfolio = model.objects.get_or_create(pk=request.user.id)[0]
            portfolio.add_balance(amount)
            return HttpResponseRedirect("/portfolio")            

    return HttpResponseRedirect("/portfolio")


    
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
    
    return render(request, 'portfolio_stock_confirm_remove.html', {'key' : key})

def remove_stock_response(request, key):
    if request.method != 'POST':
        print("Error, request should be of type post in a form")
        return HttpResponseRedirect("/portfolio")

    portfolio = PortfolioModel.objects.get_or_create(pk=request.user.id)[0]
    current_stocks = portfolio.get_stocks()
    del current_stocks[key]
    portfolio.set_stocks(current_stocks)
    portfolio.save()
    stocks = portfolio.get_stocks()
    balance = portfolio.get_balance()

    return HttpResponseRedirect("/portfolio")


    '''portfolio = PortfolioModel.objects.get_or_create(pk=request.user.id)[0]
                current_stocks = portfolio.get_stocks()
                del current_stocks[key]
                portfolio.set_stocks(current_stocks)
                portfolio.save()
                stocks = portfolio.get_stocks()
                balance = portfolio.get_balance()
            
                return render(request, 'stock_confirm_delete.html', {'object': key })'''
    #rendering a page keeps us at the delete page, we want to redirect
    #return HttpResponseRedirect("/portfolio")


def getPortfolio(request):
    portfolio = PortfolioModel.objects.get_or_create(pk=request.user.id)[0]
    stocks = portfolio.get_stocks()
    balance = portfolio.get_balance()

    return render(request, 'portfolio.html', {'portfolio': portfolio,'stocks': stocks, 'balance': balance, 'user' : request.user})

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





