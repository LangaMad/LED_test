from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionDeleteView

urlpatterns = [
    path('', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('<str:username>/', SubscriptionDeleteView.as_view(), name='subscription-delete'),
]