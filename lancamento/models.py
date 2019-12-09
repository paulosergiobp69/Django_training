from django.db import models

# Create your models here.
class TipoLancamento(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + self.descricao

class Lancamento(models.Model):

    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True, null=True)
    tipolancamento = models.ForeignKey(TipoLancamento, on_delete=models.PROTECT, related_name='tipolancamento_fk', null=True)




  