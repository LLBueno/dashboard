from django.contrib import admin
from dashboard.core import models


class ProdutoPostoTrabalhoInline(admin.TabularInline):
    model = models.ProdutoPostoTrabalho
    extra = 0


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'aviao',
    ]

    fieldsets = [
        ('Dados do Produto', {
            'fields': [
                'aviao',
                'nome',
            ]
        }),
    ]

    inlines = [ProdutoPostoTrabalhoInline]


admin.site.register(models.Aviao)
admin.site.register(models.PostoTrabalho)
admin.site.register(models.Produto, ProdutoAdmin)
