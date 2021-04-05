from django.urls import path

from . import views
from .views import calculate_distance_view

app_name = 'open_now'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/map/', calculate_distance_view, name='calculate-view')


]

