from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from snippets import views
# from employee import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
# router.register(
  # r'employee', views.LoginViewSet
# )

urlpatterns = [
  url(r'^', include(router.urls)),
]
