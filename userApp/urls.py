from django.urls import path
from .views import UserRegistration, UserLogin, UserProfile, PasswordResetRequest, PasswordReset, admin_panel

urlpatterns = [
    # user account URL
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', UserLogin.as_view(), name='user-login'),
    # profile update URL
    path('profile/', UserProfile.as_view(), name='user-profile'),
    # forgot password URL
    path('password-reset/', PasswordResetRequest.as_view(), name='password-reset-request'),
    path('password-reset/<str:uidb64>/<str:token>/', PasswordReset.as_view(), name='password-reset'),
    # admin-panel
    path('admin-panel/', admin_panel, name='admin-panel'),
]


