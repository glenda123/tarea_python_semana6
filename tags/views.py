from tags.models import Tag


from rest_framework import viewsets

from tags.serializers import TagSerializer



class TagViewSet(viewsets.ModelViewSet):
    queryset= Tag.objects.all()
    serializer_class=TagSerializer
   

# Create your views here.
