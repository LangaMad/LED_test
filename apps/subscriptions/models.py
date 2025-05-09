from django.db import models
from django.conf import settings
from ..git_data.models import GitHubProfile

# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(GitHubProfile, on_delete=models.CASCADE, related_name="subscriptions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'profile')

    def __str__(self):
        return f"{self.user.email} -> {self.profile.username}"