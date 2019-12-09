from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from django.http import HttpResponse
from lancamento.external_apis import TestRequest
from lancamento.models import TipoLancamento

def index(request):
    request_api = TestRequest()
    exchange_dict = request_api.get_rates()
    result = []
    for row in exchange_dict['rates']:
        result.append(row +' : '+ str(exchange_dict['rates'][row]))
    title = 'Exchange Rates'
    lancamento = TipoLancamento.objects.all()
    #return HttpResponse("<h1>%s</h1>" % result)

    return render(request, 'index.html', {'title': title, 'rates': result, 'tipolancamento': lancamento})
