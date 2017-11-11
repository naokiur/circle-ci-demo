"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from mysite import views
# from employee import views

router = routers.DefaultRouter()

# router.register(
#     r'news/',
#     views.Login,
#     base_name='Page'
# )

schema_view = get_swagger_view(title='Pastenbin API')

sample_urlpatterns = [
    url(r'news/', views.page_title),
]

urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'sample/', include(sample_urlpatterns))
    # url(r'^api/', include(router.urls, namespace='api')),
    # url(r'^admin/', admin.site.urls),
    # url(r'news/', views.page_title, name="page_title")
]
