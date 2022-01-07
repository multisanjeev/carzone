from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts', include('accounts.urls')),
]