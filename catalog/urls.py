from django.urls import path

from catalog.views import index
from .views import index, by_type, ItemCreateView

urlpatterns = [
    path('add/', ItemCreateView.as_view(), name='add'),
    path('<int:type_id>/', by_type, name='by_type'),
    path('', index, name='index')
]