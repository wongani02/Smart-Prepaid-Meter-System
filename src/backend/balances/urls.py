from django.urls import path

from . import views

app_name = 'balances'


urlpatterns = [
    path('', views.dashboardView, name='dashboard'),
    path('token-history', views.tokenHistoryView, name='token-history'),
]