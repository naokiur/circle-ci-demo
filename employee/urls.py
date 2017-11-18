from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from employee import views

router = routers.DefaultRouter()
router.register(
  r'employee', views.EmployeeViewSet
)
router.register(
  r'login', views.LoginUserViewSet
)


schema_view = get_swagger_view(title='Pastenbin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'swagger$', schema_view),
]
