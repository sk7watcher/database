from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ProfileDetailView, 
    UserCreateView, 
    ProfileUpdateView, 
    UserDeleteView, 
    HospitalDetailView, 
    HospitalCreateView, 
    HospitalListView,
    HospitalDeleteView)

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),

    path('hospital/<int:pk>', HospitalDetailView.as_view(), name='hospital-detail'),
    path('hospital/new', HospitalCreateView.as_view(), name='hospital-create'),
    path('hospital/', HospitalListView.as_view(), name='user-hospital-list'),
    path('hospital/<int:pk>/delete', HospitalDeleteView.as_view(), name='hospital-delete'),

    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('registration/', UserCreateView.as_view(), name='profile-create'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='user-delete'),
]
