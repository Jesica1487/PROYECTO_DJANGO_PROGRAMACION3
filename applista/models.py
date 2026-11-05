from django.db import models

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)  # Agregamos id para eliminar
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo