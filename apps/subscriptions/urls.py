from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionDeleteView, CronUpdateView

urlpatterns = [
    path('', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('<str:username>/', SubscriptionDeleteView.as_view(), name='subscription-delete'),
    path('cron/update/', CronUpdateView.as_view(), name='cron-update'),
]