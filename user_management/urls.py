from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from user_management.views import SignupView, SuccessView
app_name = "user_management"
urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('success', SuccessView.as_view(), name='success'),
]
