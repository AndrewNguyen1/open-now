from django.urls import path

from . import views

app_name = 'open_now'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('businesses/', views.BusinessView.as_view(), name='business_list'),
    path('business-form/', views.BusinessFormView.as_view(), name='business_form'),
    path('new-business/', views.get_business, name='new_business')

]

