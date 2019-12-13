from django.shortcuts import render, get_object_or_404
from django import views
from django.http import JsonResponse
from .serializers import TipoLancamentoSerializer
from rest_framework import generics, viewsets

# Create your views here.
from django.shortcuts import render
#from django.http import HttpResponse
from lancamento.external_apis import TestRequest
from lancamento.models import TipoLancamento

class IndexView(views.View):

    def get(self, request):
        request_api = TestRequest()
        exchange_dict = request_api.get_rates()
        result = []
        for row in exchange_dict['rates']:
            result.append(row +' : '+ str(exchange_dict['rates'][row]))
        title = 'Exchange Rates'
        lancamento = TipoLancamento.objects.all()
        #return HttpResponse("<h1>%s</h1>" % result)
    
        return render(request, 'index.html', {'title': title, 'rates': result, 'tipolancamento': lancamento})

class TipoLancamentoView(views.View):

    def get(self, request):
        return render(request, 'manutencao_tipo_lancamento.html')

    def post(self, request):
        descricao = request.POST.get('descricao')
        TipoLancamento.objects.create(descricao=descricao)

        return self.get(request)

class ListagemDadosView(views.View):
    def tipo_lancamento_list(request):
        MAX_OBJECTS = 20
        tipos_lancamento = TipoLancamento.objects.all()[:MAX_OBJECT]
        data = {"results": list(tipos_lancamento.values("id","descricao"))}

        return JsonResponse(data)

    def tipo_lancamento_detail(request, pk):
        tipo_lancamento = get_object_or_404(TipoLancamento, pk=pk)
        data = {"results": {
            "id": tipo_lancamento.id,
            "descricao": tipo_lancamento.descricao
        }}
        
        return JsonResponse(data)

class TipoLancamentoAPI(viewsets.ModelViewSet):
    queryset = TipoLancamento.objects.all().order_by('id')
    serializer_class = TipoLancamentoSerializer


        
        
