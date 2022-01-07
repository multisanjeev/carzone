from django.urls import path

urlpatterns = [
    path('login', views.login, 'login'),
    path('register', views.register, 'register'),
    path('logout', views.logout, 'logout'),
    path('dashboard', views.dashboard, 'dashboard'),
]