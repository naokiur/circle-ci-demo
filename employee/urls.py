from django.conf.urls import url, include
from rest_framework import routers

from employee import views

router = routers.DefaultRouter()
router.register(
  r'employee', views.EmployeeViewSet
)
router.register(
  r'login', views.LoginUserViewSet
)

urlpatterns = [
    url(r'^', include(router.urls))
]
