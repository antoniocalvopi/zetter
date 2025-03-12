from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    # Reemplazamos `tags` y `related_notes` por `relation`
    relation = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(), many=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'relation', 'created_at', 'updated_at', 'author']

    def create(self, validated_data):
        # Asigna automáticamente el 'author' al usuario autenticado
        user = self.context['request'].user  # Obtiene el usuario desde la solicitud
        validated_data['author'] = user  # Asigna el usuario autenticado al campo 'author'
        return super().create(validated_data)