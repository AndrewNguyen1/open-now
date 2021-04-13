from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'open_now'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('businesses/', views.BusinessView.as_view(), name='business_list'),
    path('business-form/', views.BusinessFormView.as_view(), name='business_form'),
    path('new-business/', views.get_business, name='new_business'),
    path('search/', views.search_business, name='search_result'),
    path('new-forum/', views.new_forum, name='new_forum'),
    path('new-discussion/', views.new_discussion, name='new_discussion'),
    path('forums/', views.forums, name='forums'),
    path('admin/', admin.site.urls),
    path('business-form/create-businessimage/', views.create_businessimage, name = 'create_businessimage')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)