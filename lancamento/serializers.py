from rest_framework import serializers
from .models import TipoLancamento


class TipoLancamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLancamento
        fields = '__all__'
        