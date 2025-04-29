from rest_framework import serializers
from .models import Subscription
from ..git_data.serializers import GitHubProfileSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    profile = GitHubProfileSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ['profile', 'created_at']
