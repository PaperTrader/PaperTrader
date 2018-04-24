"""PaperTrader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import PaperTraderApp.views
from PaperTraderApp.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaperTraderApp.views.ListStockView.as_view(), name="Home"),
    path('stock-list/', PaperTraderApp.views.ListStockView.as_view(), name="stock-list"),
    path('create-stock/', PaperTraderApp.views.CreateStockView.as_view(), name="stock-new"),
    path('delete-stock/<int:pk>', PaperTraderApp.views.DeleteStockView.as_view(), name="stock-delete"),
    path('delete-portfolio-stock/<str:key>', delete_from_portfolio, name="portfolio-remove"),
    path('sell-stock-response/<str:key>', sell_stock_response, name="sell-stock-response"),

    #path('portfolio', PaperTraderApp.views.PortfolioView.as_view(), name="portfolio"),
    path('portfolio', getPortfolio, name="portfolio"),
    path('add-cash', add_cash, name="add-cash"),
    path('add-cash-response', add_cash_response, name="add-cash-response"),


    path('update_stock_info', update_stock_info, name="update"),
    path('add_to_portfolio/<int:pk>', add_to_portfolio, name="portfolio-add"),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
    path('signup/', signup, name="signup"),
]
