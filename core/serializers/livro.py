from rest_framework.serializers import ModelSerializer

from core.models import Livro

class LivroGetSerializer(ModelSerializer):
    class Meta:    
        model = Livro
        fields = "__all__"
        depth = 1

class LivroSetSerializer(ModelSerializer):
    class Meta:    
        model = Livro
        fields = "__all__"