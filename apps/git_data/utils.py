import requests
from datetime import datetime
from .models import GitHubProfile

GITHUB_API_URL = 'https://api.github.com'


def fetch_github_profile_data(profile: GitHubProfile):
    username = profile.username
    repo_url = f"{GITHUB_API_URL}/users/{username}/repos?per_page=100"
    repos_response = requests.get(repo_url)

    if repos_response.status_code != 200:
        return
    repos = repos_response.json()
    profile.repo_count = len(repos)

    sorted_repos = sorted(repos, key=lambda x: x['created_at'], reverse=True)
    profile.recent_repos = [repo['name'] for repo in sorted_repos[:5]]

    language_count = {}
    for repo in repos:
        lang = repo.get('language')
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1

    popular_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    profile.popular_languages = [lang for lang, _ in popular_languages[:3]]

    commit_dates = []
    for repo in repos[:5]:
        commits_url = repo['commits_url'].split('{')[0]
        commits_resp = requests.get(commits_url)
        if commits_resp.status_code == 200:
            commits = commits_resp.json()
            if commits:
                date_str = commits[0]['commit']['committer']['date']
                try:
                    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    commit_dates.append(date_obj)
                except ValueError:
                    continue

    if commit_dates:
        profile.last_commit = max(commit_dates)

    profile.save()
