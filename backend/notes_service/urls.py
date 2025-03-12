from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateDestroyView, DeleteAllNotesView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note_list_create'),  # Crear y listar notas
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note_detail'),  # actualizar, eliminar)
    path('notes/delete_all/', DeleteAllNotesView.as_view(), name='delete_all_notes'),
]