from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 
from django.urls import include, path


from media.router import router as media_router
from rest_framework.routers import DefaultRouter

from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet


router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/media/", include(media_router.urls)),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
