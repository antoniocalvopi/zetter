from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

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
        if related_notes: 
            note.related_notes.set(related_notes)
            print(f"📝 Relaciones de notas añadidas: {related_notes}")
        else:
            print("⚠️ No hay relaciones de notas para asignar, continuando...")

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
        
        if not serializer.is_valid():
            print(f"❌ Errores de validación: {serializer.errors}")
            return

        try:
            updated_note = serializer.save()
            print(f"✅ Nota actualizada correctamente: {updated_note.id}")

            # Manejar relaciones
            related_notes = serializer.validated_data.get('relation', [])
            if related_notes:
                updated_note.related_notes.set(related_notes)
                print(f"📝 Relaciones de notas añadidas: {related_notes}")
            else:
                print("⚠️ No hay relaciones de notas para asignar, continuando...")

            print(f"📝 Relaciones actualizadas: {updated_note.related_notes.all()}")

        except Exception as e:
            print(f"❌ Error al actualizar la nota: {e}")

    def perform_destroy(self, instance):
        # Verificar que el usuario autenticado es el autor de la nota antes de eliminar
        print(f"🛑 Intentando eliminar la nota con ID: {instance.id}")
        
        # Verificar que el autor de la nota es el usuario autenticado
        if instance.author != self.request.user:
            print(f"🚫 Permiso denegado: El usuario {self.request.user} no es el autor de la nota.")
            raise PermissionDenied("No tienes permiso para eliminar esta nota.")
        
        # Eliminar la nota
        print(f"✔️ Usuario autorizado para eliminar la nota con ID: {instance.id}")
        instance.delete()
        print(f"🗑️ Nota con ID {instance.id} eliminada.")
        
class DeleteAllNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("No tienes permiso para eliminar todas las notas.")

        notes = Note.objects.filter(author=request.user)
        print(f"Notas encontradas para eliminar: {notes.count()}")
        
        # Eliminar las notas
        deleted_count, _ = notes.delete()
        print(f"Notas eliminadas: {deleted_count}")
        
        if deleted_count == 0:
            print("⚠️ No se eliminaron notas, revisa las relaciones o el autor.")
        return Response({"message": "Todas las notas han sido eliminadas."}, status=status.HTTP_204_NO_CONTENT)
