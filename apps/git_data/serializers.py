from rest_framework import serializers
from .models import GitHubProfile

class GitHubProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubProfile
        fields = '__all__'
