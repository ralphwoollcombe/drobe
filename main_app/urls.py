from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.MyProfile.as_view(), name='my-profile'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile-create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    
    path('my-drobe/', views.GarmentList.as_view(), name='garment-index'),
    path('my-drobe/<int:pk>/', views.GarmentDetail.as_view(), name='garment-detail'),
    path('my-drobe/create/', views.GarmentCreate.as_view(), name='garment-create'),
    path('my-drobe/<int:pk>/update/', views.GarmentUpdate.as_view(), name='garment-update'),
    path('my-drobe/<int:pk>/delete/', views.GarmentDelete.as_view(), name='garment-delete'),
    path('my-drobe/<int:pk>/initiate-transaction/', views.initiate_transaction, name='initiate-transaction'),

    path('communities/', views.CommunityList.as_view(), name='community-index'),
    path('communities/<int:pk>/', views.CommunityDetail.as_view(), name='community-detail'),
    path('communities/create/', views.CommunityCreate.as_view(), name='community-create'),
    path('communities/<int:pk>/update/', views.CommunityUpdate.as_view(), name='community-update'),
    path('communities/<int:pk>/delete/', views.CommunityDelete.as_view(), name='community-delete'),
    path('communities/<int:community_id>/associate-member/<int:user_id>/', views.associate_member, name='associate-member'),
    path('communities/<int:community_id>/remove-member/<int:user_id>/', views.remove_member, name='remove-member'),

    path('transactions/', views.TransactionList.as_view(), name='transaction-index'),
    path('transactions/<int:pk>/approve/', views.approve_transaction, name='approve-transaction'),
    path('transactions/<int:pk>/decline/', views.decline_transaction, name='decline-transaction'),

    path('accounts/signup/', views.signup, name='signup'),

]
