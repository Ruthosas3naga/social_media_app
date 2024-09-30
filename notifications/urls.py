from django.urls import path
from .views import CreateNotificationView, NotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/create/', CreateNotificationView.as_view(), name='create-notification'),
]