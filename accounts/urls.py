from django.urls import path
from accounts.views import RegisterView, LoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),  # Changed user_id to pk
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),  # Changed user_id to pk
    # Profile management routes can be added here
]
