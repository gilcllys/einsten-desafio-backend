from rest_framework import routers
from core import viewsets


router = routers.SimpleRouter()
router.register(r'user', viewsets.UserViewSet)
router.register(r'paciente', viewsets.PacienteViewSet)
router.register(r'saneamento_info', viewsets.SaneamentoInfoViewSet)


urlpatterns = router.urls
