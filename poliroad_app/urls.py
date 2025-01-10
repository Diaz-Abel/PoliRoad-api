from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import CarreraView, MateriaView, FacultadView

router = routers.DefaultRouter()
router.register(r"carreras", CarreraView)
router.register(r"materias", MateriaView)
router.register(r"facultades", FacultadView)

urlpatterns = [
    path("api/", include(router.urls)),
    path("docs/", include_docs_urls(title="PoliMap API")),
]
