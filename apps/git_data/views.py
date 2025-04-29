from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import GitHubProfile
from .serializers import GitHubProfileSerializer

class GitHubProfileDetailView(generics.RetrieveAPIView):
    queryset = GitHubProfile.objects.all()
    serializer_class = GitHubProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
