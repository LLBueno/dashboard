from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from dashboard.core.models import Produto, Aviao
import json


def index(request):
    return render(request, 'login.html')


class ProdutoListView(ListView):
    template_name = 'core/produto_list.html'
    model = Produto
    paginate_by = 10


class ProdutoDetailView(DetailView):
    template_name = 'core/produto_detail.html'
    model = Produto
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ProdutoDetailView, self).get_context_data(**kwargs)
        context['postostrabalho'] = self.object.produtopostotrabalho_set.all()
        return context


class AviaoListView(ListView):
    template_name = 'core/aviao_list.html'
    model = Aviao
    paginate_by = 10


class AviaoDetailView(DetailView):
    template_name = 'core/aviao_detail.html'
    model = Aviao
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AviaoDetailView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.filter(aviao=self.object)
        return context


class ProdutosChartView(TemplateView):
    template_name = 'core/produtos_grafico.html'

    def json_grafico(self):
        results = [
            {
                "label": "Atrasados",
                "value": 0,
                "color": "#d92550"
            },
            {
                "label": "Adiantados",
                "value": 0,
                "color": "#3f6ad8"
            },
            {
                "label": "Em dia",
                "value": 0,
                "color": "#3ac47d"
            },
        ]
        produtos = Produto.objects.all()
        for produto in produtos:
            if produto.media_atraso is not None:
                if produto.media_atraso < 0:
                    results[0]['value'] += 1
                elif produto.media_atraso > 0:
                    results[1]['value'] += 1
                else:
                    results[2]['value'] += 1
        return json.dumps(results)

    def get_context_data(self, **kwargs):
        context = super(ProdutosChartView, self).get_context_data(**kwargs)
        context['data_chart'] = self.json_grafico()
        return context
