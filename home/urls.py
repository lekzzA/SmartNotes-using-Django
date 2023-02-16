from django.urls import path 
from . import views

urlpatterns  = [
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.AuthorizedView.as_view()),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('signup', views.UserSignupView.as_view(), name='signup'),
]