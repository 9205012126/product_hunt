
from django.contrib import admin
from django.urls import path,include
from products import views
from accounts import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/',include('accounts.urls'), name='account'),
]
