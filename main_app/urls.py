from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name='profile-detail'),
    path('my-drobe/', views.GarmentList.as_view(), name='garment-index'),
    path('my-drobe/<int:pk>/', views.GarmentDetail.as_view(), name='garment-detail'),
    path('my-drobe/create/', views.GarmentCreate.as_view(), name='garment-create'),
    path('my-drobe/<int:pk>/update', views.GarmentUpdate.as_view(), name='garment-update'),
    path('my-drobe/<int:pk>/delete', views.GarmentDelete.as_view(), name='garment-delete'),

    path('accounts/signup/', views.signup, name='signup'),

]
