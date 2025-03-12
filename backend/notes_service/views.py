from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(f"➡️ Solicitud de creación de nota recibida")
        print(f"🧑‍🤝‍🧑 Usuario autenticado: {self.request.user}")
        print(f"📦 Datos del serializer antes de guardar: {serializer.validated_data}")

        note = serializer.save(author=self.request.user)

        print(f"✅ Nota guardada con autor: {self.request.user}")

        related_notes = serializer.validated_data.get('relation', [])
        note.related_notes.set(related_notes) 

        print(f"📝 Relaciones de notas añadidas: {related_notes}")

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Mostrar el ID de la nota y el usuario que hace la solicitud
        print(f"🔍 Verificando permiso de acceso para la nota")

        # Obtenemos la nota que se va a recuperar
        note = super().get_object()
        print(f"📑 Nota obtenida: {note.title} (ID: {note.id})")

        # Verificar que el autor de la nota es el usuario autenticado
        if note.author != self.request.user:
            print(f"🚫 Permiso denegado: El usuario {self.request.user} no es el autor de la nota.")
            raise PermissionDenied("No tienes permiso para modificar esta nota.")

        print(f"✔️ Usuario autorizado a acceder a la nota.")
        return note

    def perform_update(self, serializer):
        # Guardar la actualización de la nota
        print(f"➡️ Actualizando la nota con los nuevos datos")
        updated_note = serializer.save()

        # Aquí manejamos las relaciones durante la actualización de la nota
        related_notes = serializer.validated_data.get('relation', [])
        updated_note.related_notes.set(related_notes)  # Actualizar las relaciones de notas

        # Confirmación de relaciones actualizadas
        print(f"📝 Relaciones actualizadas: {related_notes}")