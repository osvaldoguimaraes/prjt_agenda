from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.olhar_contato, name='olhar_contato'),
]
