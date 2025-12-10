from django.urls import path
from .views import index, projeto_detail

urlpatterns = [
    path('', index, name='index'),
    path('projeto/<int:pk>/', projeto_detail, name='projeto_detail')
]