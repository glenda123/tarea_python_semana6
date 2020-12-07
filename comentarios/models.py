from django.db import models

# Create your models here.
class Comentario(models.Model):
    autor=models.CharField(max_length=200)
    fecha_comentario=models.DateField()
    contenido=models.CharField(max_length=2000)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.contenido