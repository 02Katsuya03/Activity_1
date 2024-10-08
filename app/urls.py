from django.urls import path
from .views import BasePageView, HomePageView, AboutPageView

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('Home', HomePageView.as_view(), name='Home'),
    path('About', AboutPageView.as_view(), name='About'),
]