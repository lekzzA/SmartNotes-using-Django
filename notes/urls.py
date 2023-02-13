from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.DetailedView.as_view()),
]
