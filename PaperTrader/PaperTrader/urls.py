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
from PaperTraderApp.views import update_stock_info, add_to_portfolio
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaperTraderApp.views.ListStockView.as_view(), name="Home"),
    path('stock-list/', PaperTraderApp.views.ListStockView.as_view(), name="stock-list"),
    path('create-stock/', PaperTraderApp.views.CreateStockView.as_view(), name="stock-new"),
    path('delete-stock/<int:pk>', PaperTraderApp.views.DeleteStockView.as_view(), name="stock-delete"),
    path('delte-portfolio-stock/<int:pk>', PaperTraderApp.views.DeleteFromPortfolioView.as_view(), name="portfolio-remove"),
    path('portfolio', PaperTraderApp.views.PortfolioView.as_view(), name="portfolio"),
    path('update_stock_info', update_stock_info, name="update"),
    path('add_to_portfolio/<int:pk>/<str:user>', add_to_portfolio, name="portfolio-add"),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
]
