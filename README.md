Проект позволяет пользователям подписываться на GitHub-профили, получать информацию о них (репозитории, популярные языки, дата последнего коммита) и обновлять эти данные.

📦 Стек технологий
Python 3.10+

Django

Django REST Framework

Djoser (регистрация и аутентификация через JWT)

GitHub API

🚀 Быстрый старт
1. 🔧 Клонируй репозиторий и установи зависимости

``` 
git clone git@github.com:LangaMad/LED_test.git
cd Led
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. 📂 Применяй миграции и создай суперпользователя

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
3. ▶️ Запусти сервер
```
python manage.py runserver
```
👤 Аутентификация (JWT)
Используется библиотека Djoser для регистрации и входа.
🔐 Регистрация
POST /auth/users/
```
{
  "email": "example@mail.com",
  "password": "your_password"
}
```
🔑 Получение токенов
```
{
  "email": "example@mail.com",
  "password": "your_password"
}
```
Ответ:
```
{
  "access": "токен",
  "refresh": "токен"
}
```

📬 Подписки
➕ Подписка на GitHub-профиль
POST /subscriptions/
```
{
  "username": "octocat"
}
```
🧠 Данные о GitHub-профиле
📄 Получить данные по нику
GET /git_data/<username>/

Ответ:
```
{
  "username": "octocat",
  "repo_count": 5,
  "popular_languages": ["Python", "JavaScript"],
  "last_commit_date": "2025-04-30T10:20:00Z",
  "last_updated": "2025-04-30T10:30:00Z"
}
```

🔁 Обновить все подписки
GET /subscriptions/cron/update/

Ответ:

```
{
  "detail": "2 GitHub профилей обновлено.",
  "updated_profiles": [
    {
      "username": "octocat",
      "repo_count": 5,
      "popular_languages": ["Python", "Go"],
      ...
    },
    ...
  ]
}
```























