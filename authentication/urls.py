from django.urls import path
from . import views

urlpatterns = [

    path('register',views.registration,name='register'),
    path('login',views.user_login,name='login'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('logout',views.user_logout,name='logout'),
]