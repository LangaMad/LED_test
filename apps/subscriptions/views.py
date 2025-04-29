from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from ..git_data.models import GitHubProfile
from .serializers import SubscriptionSerializer
# from git_data.utils import fetch_github_profile_data  # мы создадим эту функцию

class SubscriptionListCreateView(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if not username:
            return Response({"detail": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        profile, _ = GitHubProfile.objects.get_or_create(username=username)
        # fetch_github_profile_data(profile)  # наполняем данными

        # создать подписку
        subscription, created = Subscription.objects.get_or_create(
            user=request.user,
            profile=profile
        )
        if not created:
            return Response({"detail": "Already subscribed"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class SubscriptionDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    def delete(self, request, username):
        try:
            profile = GitHubProfile.objects.get(username=username)
            subscription = Subscription.objects.get(user=request.user, profile=profile)
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GitHubProfile.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        except Subscription.DoesNotExist:
            return Response({"detail": "Not subscribed"}, status=status.HTTP_400_BAD_REQUEST)
