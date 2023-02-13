from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.listnote),
    path('notes/<int:pk>', views.detail),
]
