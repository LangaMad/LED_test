from django.contrib import admin
from .models import GitHubProfile
# Register your models here.


@admin.register(GitHubProfile)
class GitProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'public_repos', 'last_commit', 'updated_at')
    search_fields = ('username',)
