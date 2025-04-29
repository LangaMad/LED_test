from django.contrib import admin
from .models import Subscription
# Register your models here.


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'profile__username')