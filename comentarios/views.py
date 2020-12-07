

# Create your views here.
from comentarios.models import Comentario


from rest_framework import viewsets

from comentarios.serializers import ComentarioSerializer



class ComentarioViewSet(viewsets.ModelViewSet):
    queryset= Comentario.objects.all()
    serializer_class=ComentarioSerializer
   