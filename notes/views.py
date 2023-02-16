from django.shortcuts import render
from .forms import NotesForm

# Create your views here.
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView,ListView,DetailView, UpdateView
from django.views.generic.edit import DeleteView

class NotesDeleteView(DeleteView):
    model=Notes
    success_url = '/smart/notes'
    template_name='notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/note_list.html'

# def listnote(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/note_list.html', {'notes': all_notes})

class DetailedView(DetailView):
    model = Notes
    context_object_name = ("note")
    template_name = "notes/notes_details.html"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         return render(request, 'notes/404_Exception.html', {})
#         # raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_details.html', {'note': note})