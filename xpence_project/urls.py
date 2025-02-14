"""xpence_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import lancamento, autenticacao
from . import views
from rest_framework.routers import DefaultRouter
from lancamento import views as lancamento
from autenticacao import views as autenticacao


router = DefaultRouter()
#
router.register(r'tipolancamentoviewapi', lancamento.TipoLancamentoAPI)
router.register(r'users', autenticacao.UserViewSet, basename='user')


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('lancamento/', include('lancamento.urls')),
    #path('autenticacao/', include('autenticacao.urls')),
    url(r'^', include(router.urls))
]
