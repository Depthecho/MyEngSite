from .services import NotificationService

def notifications_context(request):
    unread_notifications_count = 0
    if request.user.is_authenticated:
        unread_notifications_count = NotificationService.get_unread_count(request.user)
    return {
        'unread_notifications_count': unread_notifications_count
    }