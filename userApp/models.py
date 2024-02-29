from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_password_token_created_at = models.DateTimeField(blank=True, null=True)

    def reset_password_valid(self):
        return self.reset_password_token_created_at and \
               (timezone.now() - self.reset_password_token_created_at).seconds < 3600  # 1 hour validity period
