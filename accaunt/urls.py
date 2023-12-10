from django.urls import path

from . import views

urlpatterns = [
    path('sing-up/', views.signup_view),
    path('sing-in/', views.signin_view),
    path('log-out/', views.logout_view),
]