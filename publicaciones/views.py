
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from publicaciones.models import Publicacion
from tags.models import Tag
from comentarios.models import Comentario
from rest_framework import viewsets
from rest_framework.decorators import action
from tags.serializers import TagSerializer
from comentarios.serializers import ComentarioSerializer
from publicaciones.serializers import PublicacionSerializer
from rest_framework.response import Response
from rest_framework import status


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset= Publicacion.objects.all()
    serializer_class=PublicacionSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True) 
    def tags(self, request, pk=None):
        
        publicacion= self.get_object()

        if request.method=='GET':

            serialized= TagSerializer(publicacion.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method=='POST':
            tags_id= request.data['tags_ids']
            print(tags_id)
            for tag_id in tags_id:
                tag=Tag.objects.get(id=int(tag_id))
                publicacion.tags.add(tag)
            return Response(status=status.HTTP_200_OK)

        if request.method=='DELETE':
            tags_id = request.data['tags_ids']
            
            for tag_id in tags_id:
                tag=Tag.objects.get(id=int(tag_id))
                publicacion.tags.remove(tag)
            return Response(status=status.HTTP_200_OK)


    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def comentarios(self, request, pk=None):
        
        publicacion= self.get_object()

        if request.method=='GET':

            serialized= ComentarioSerializer(publicacion.comentarios, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method=='POST':
            comentarios_id= request.data['comentarios_ids']
            print(comentarios_id)
            for comentario_id in comentarios_id:
                comentario=Comentario.objects.get(id=int(comentario_id))
                publicacion.comentarios.add(comentario)
            return Response(status=status.HTTP_200_OK)

        if request.method=='DELETE':
            comentarios_id = request.data['comentarios_ids']
            
            for comentario_id in comentarios_id:
                comentario=Comentario.objects.get(id=int(comentario_id))
                publicacion.comentarios.remove(comentario)
            return Response(status=status.HTTP_200_OK)
   