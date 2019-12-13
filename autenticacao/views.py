from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404 
from .serializers import UserSerializer 
from rest_framework import viewsets 
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """ A simple ViewSet for listing or retrieving users. """
    serializer_class = UserSerializer 
    queryset = User.objects.all()

    """
    def list(self, request): 
        queryset = User.objects.all() 
        serializer = UserSerializer(queryset, many=True) 
        return Response(serializer.data)

    def retrieve(self, request, pk=None): 
        queryset = User.objects.all() 
        user = get_object_or_404(queryset, pk=pk) 
        serializer = UserSerializer(user) 
        return Response(serializer.data)

    def post(self, request):

        descricao = request.POST.get('descricao')
        TipoLancamento.objects.create(descricao=descricao)

        return self.get(request)
    """