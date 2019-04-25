from django.urls import path
from user_management.views import SignupView, SuccessView, ProfileView

app_name = "user_management"
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('success/', SuccessView.as_view(), name='success'),
    path('profile/', ProfileView.as_view(), name='profile')
]
