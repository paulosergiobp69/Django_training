from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tipo_lancamento_insert/', views.TipoLancamentoView.as_view(), name='tipo_lancamento_insert'),
    path('tipo_lancamento_list/', views.ListagemDadosView.tipo_lancamento_list, name='tipo_lancamento_list'),
    path('tipo_lancamento_detail/<int:pk>/', views.ListagemDadosView.tipo_lancamento_detail, name='tipo_lancamento_detail'),
    

]