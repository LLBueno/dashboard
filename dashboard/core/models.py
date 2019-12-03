from django.db import models
import numpy as np
from django.utils.html import format_html


class Aviao(models.Model):
    numero = models.CharField('número', max_length=7, blank=False, null=False)

    class Meta:
        verbose_name = 'Avião'
        verbose_name_plural = 'Aviões'

    def __str__(self):
        return self.numero


class PostoTrabalho(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Posto de Trabalho'
        verbose_name_plural = 'Postos de Trabalho'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    aviao = models.ForeignKey(Aviao, blank=False, null=False, on_delete=models.PROTECT, verbose_name='avião')
    postos = models.ManyToManyField(
        PostoTrabalho,
        through='ProdutoPostoTrabalho',
        through_fields=('produto', 'posto_trabalho'),
    )

    def get_feriados(self):
        return [x.data for x in Feriado.objects.all()]

    @property
    def media_atraso(self):
        if not self.produtopostotrabalho_set.exists():
            return None
        media = 0
        for posto in self.produtopostotrabalho_set.all():
            if posto.data_inicio_planejada and posto.data_inicio_real:
                diff_data = np.busday_count(posto.data_inicio_real.date(), posto.data_inicio_planejada.date(), holidays=self.get_feriados())
                media += diff_data
        return media

    @property
    def get_image(self):
        return format_html('<img src="{% static \'images\' %}">')

    def __str__(self):
        return self.nome


class ProdutoPostoTrabalho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    posto_trabalho = models.ForeignKey(PostoTrabalho, on_delete=models.CASCADE)
    data_inicio_planejada = models.DateTimeField()
    data_final_planejada = models.DateTimeField()
    data_inicio_real = models.DateTimeField(blank=True, null=True)
    data_final_real = models.DateTimeField(blank=True, null=True)

    def get_feriados(self):
        return [x.data for x in Feriado.objects.all()]

    @property
    def media_atraso(self):
        if self.data_final_planejada and self.data_final_real:
            return np.busday_count(self.data_final_real.date(), self.data_final_planejada.date(), holidays=self.get_feriados())
        elif self.data_inicio_planejada and self.data_inicio_real:
            return np.busday_count(self.data_inicio_real.date(), self.data_inicio_planejada.date(), holidays=self.get_feriados())
        return None

    class Meta:
        verbose_name = 'Posto de Trabalho'
        verbose_name_plural = 'Postos de Trabalho'
        ordering = ['data_inicio_planejada']

    def __str__(self):
        return self.posto_trabalho.nome


class Feriado(models.Model):
    nome = models.CharField(max_length=25, blank=False, null=False)
    data = models.DateField(blank=False, null=False)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.nome


class CSV(models.Model):
    arquivo = models.FileField()
