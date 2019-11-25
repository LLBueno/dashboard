from django.urls import path

from dashboard.core import views

urlpatterns = [
    path('produto/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produto/<pk>/detail/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('aviao/', views.AviaoListView.as_view(), name='aviao_list'),
    path('aviao/<pk>/detail/', views.AviaoDetailView.as_view(), name='aviao_detail'),
    path('produtos/grafico/', views.ProdutosChartView.as_view(), name='aviao_grafico'),
]
