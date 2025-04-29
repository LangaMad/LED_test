from django.contrib import admin
from .models import GitHubProfile
# Register your models here.

@admin.register(GitHubProfile)
class GitProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'repo_count', 'last_commit_date', 'last_updated')  # Исправлены поля
    search_fields = ('username',)
    list_filter = ('last_updated',)
