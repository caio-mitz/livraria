from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Livro
from media.models import Image
from media.serializers import ImageSerializer


class LivroGetSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:    
        model = Livro
        fields = "__all__"
        depth = 1

class LivroSetSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Livro
        fields = "__all__"