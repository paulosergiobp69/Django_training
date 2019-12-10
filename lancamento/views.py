from django.shortcuts import render
from django import views

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
