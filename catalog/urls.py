from django.urls import path

from catalog.views import index
from .views import index, by_type

urlpatterns = [
    path('<int:type_id>/', by_type),
    path('', index)
]