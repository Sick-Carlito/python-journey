# quotes/urls.py

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote_list, name='quote-list'),
]

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_quote, name='add_quote'),  # New URL for adding quotes
]
