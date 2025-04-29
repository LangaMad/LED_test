# profiles/urls.py
from django.urls import path
from .views import GitHubProfileDetailView

urlpatterns = [
    path('<str:username>/', GitHubProfileDetailView.as_view(), name='profile-detail'),
]
