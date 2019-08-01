
from django.contrib import admin
from django.urls import path,include
from products import views
from accounts import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/',include('accounts.urls'), name='account'),
    path('product/', include('products.urls'), name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
