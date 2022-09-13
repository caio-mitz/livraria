from rest_framework.viewsets import ModelViewSet

from core.models import Editora, Livro
from core.serializers import LivroGetSerializer, LivroSetSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroGetSerializer
        return LivroSetSerializer