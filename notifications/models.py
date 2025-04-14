from django.db import models
from django.conf import settings
from django.utils import timezone

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('budget_alert', 'Budget Alert'),
        ('savings_goal', 'Savings Goal Update'),
        ('system', 'System Notification'),
        ('fraud_alert', 'Fraud Alert'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_notification_type_display()} - {self.title}"

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save()
