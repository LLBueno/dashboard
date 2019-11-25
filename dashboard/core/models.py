from django.db import models


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

    @property
    def media_atraso(self):
        if not self.produtopostotrabalho_set.exists():
            return None
        media = 0
        for posto in self.produtopostotrabalho_set.all():
            if posto.data_inicio_planejada and posto.data_inicio_real:
                diff_data = posto.data_inicio_planejada.date() - posto.data_inicio_real.date()
                media += diff_data.days
        return media

    def __str__(self):
        return self.nome


class ProdutoPostoTrabalho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    posto_trabalho = models.ForeignKey(PostoTrabalho, on_delete=models.CASCADE)
    data_inicio_planejada = models.DateTimeField()
    data_final_planejada = models.DateTimeField()
    data_inicio_real = models.DateTimeField(blank=True, null=True)
    data_final_real = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Posto de Trabalho'
        verbose_name_plural = 'Postos de Trabalho'
        ordering = ['data_inicio_planejada']

    def __str__(self):
        return self.posto_trabalho.nome


class CSV(models.Model):
    arquivo = models.FileField()
