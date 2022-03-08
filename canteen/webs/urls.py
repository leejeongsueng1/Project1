from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('map/', views.map, name='map'),
    path('map2/', views.map2, name='map'),
    path('about_us', views.about_us, name='about_us'),
    path('graph/',views.graph, name='graph'),
    ]







