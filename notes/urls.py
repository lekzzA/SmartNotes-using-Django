from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="note.list"),
    path('notes/<int:pk>', views.DetailedView.as_view(), name="note.detail"),
]
