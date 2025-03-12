from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateDestroyView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note_list_create'),  # Crear y listar notas
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note_detail'),  # Detalles de una nota (ver, actualizar, eliminar)
]