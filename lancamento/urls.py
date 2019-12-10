from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tipo_lancamento_insert/', views.TipoLancamentoView.as_view(), name='tipo_lancamento_insert')
]