from django.contrib import admin
from django.urls import path
from academiadata.views import AlunoViewSet, ModalidadeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='alunos')
router.register('modalidades', ModalidadeViewSet, basename='modalidades')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
