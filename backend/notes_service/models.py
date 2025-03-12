from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)  # Título opcional
    content = models.TextField()  # Contenido de la nota
    relation = models.ManyToManyField('self', blank=True)  # Notas relacionadas (auto-referencia)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última modificación
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que crea la nota

    def __str__(self):
        return self.title or f"Nota {self.id}"