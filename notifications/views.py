from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Notification

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    unread_count = notifications.filter(is_read=False).count()
    return render(request, 'notifications/notifications.html', {
        'notifications': notifications,
        'unread_count': unread_count
    })

@login_required
def mark_notification_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.mark_as_read()
    messages.success(request, 'Notification marked as read!')
    return redirect('notifications')

@login_required
def mark_all_notifications_read(request):
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    for notification in unread_notifications:
        notification.mark_as_read()
    messages.success(request, 'All notifications marked as read!')
    return redirect('notifications')
