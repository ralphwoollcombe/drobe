from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('my-drobe/', views.GarmentList.as_view(), name='garment-index')
]
