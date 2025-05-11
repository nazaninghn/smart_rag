from django.urls import path
from .views import home, upload_file, agent_view

urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_file, name="upload"),
    path("agent/", agent_view, name="agent"),
]
