from django.urls import path
from .views import home, upload_file, agent_view
from .api import RAGApi

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_file, name='upload'),
    path('agent/', agent_view, name='agent'),
    path('api/', RAGApi.as_view(), name='api'),
]
