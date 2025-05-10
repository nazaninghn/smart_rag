from django.urls import path
from .views import home
from .api import RAGApi

urlpatterns = [
    path('', home),
    path('api/', RAGApi.as_view())
]
