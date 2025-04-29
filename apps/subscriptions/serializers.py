import requests
from rest_framework import serializers
from .models import Subscription
from ..git_data.models import GitHubProfile


class SubscriptionSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'username', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        import requests
        from datetime import datetime

        user = self.context['request'].user
        username = validated_data['username']

        # Получаем или создаём GitHubProfile
        profile, created = GitHubProfile.objects.get_or_create(username=username)

        if created:
            user_url = f'https://api.github.com/users/{username}'
            repos_url = f'https://api.github.com/users/{username}/repos?per_page=100&sort=updated'

            user_resp = requests.get(user_url)
            repos_resp = requests.get(repos_url)

            if user_resp.status_code != 200:
                raise serializers.ValidationError("GitHub user not found")

            user_data = user_resp.json()
            repos_data = repos_resp.json() if repos_resp.status_code == 200 else []

            profile.repo_count = user_data.get("public_repos", 0)

            commit_dates = [
                repo.get("pushed_at") for repo in repos_data if repo.get("pushed_at")
            ]
            if commit_dates:
                latest_commit = max(commit_dates)
                profile.last_commit_date = datetime.strptime(latest_commit, "%Y-%m-%dT%H:%M:%SZ")

            languages = [repo.get("language") for repo in repos_data if repo.get("language")]
            from collections import Counter
            top_languages = [lang for lang, _ in Counter(languages).most_common(3)]
            profile.popular_languages = top_languages

            profile.last_updated = datetime.utcnow()

            profile.save()

        subscription, _ = Subscription.objects.get_or_create(user=user, github_profile=profile)
        return subscription



