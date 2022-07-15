from django.contrib import admin 
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroGetViewSet, LivroSetViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'livrosget', LivroGetViewSet)
router.register(r'livrosset', LivroSetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]