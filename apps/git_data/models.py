from django.db import models

# Create your models here.
class GitHubProfile(models.Model):
    username = models.CharField('Username',max_length=39, unique=True)  # GitHub username
    repo_count = models.IntegerField('Количество репозиториев',default=0)
    popular_languages = models.JSONField('Популярные языки',default=list)  # например: ["Python", "JavaScript"]
    last_commit_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username