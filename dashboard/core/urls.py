from django.urls import path

from dashboard.core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('linha/', views.ProdutoListView.as_view(), name='produto_list'),
    path('linha/<pk>/detail/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('range/', views.AviaoListView.as_view(), name='aviao_list'),
    path('range/<pk>/detail/', views.AviaoDetailView.as_view(), name='aviao_detail'),
    path('range/grafico/', views.ProdutosChartView.as_view(), name='aviao_grafico'),
    path('slideshow/', views.SlideshowView.as_view(), name='slideshow'),
]
