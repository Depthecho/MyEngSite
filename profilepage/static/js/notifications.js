const markAllReadBtn = document.getElementById('mark-all-read-btn');

    if (markAllReadBtn) {
        markAllReadBtn.addEventListener('click', function(event) {
            event.preventDefault();

            fetch('/profile/notifications/mark_all_as_read/', {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(handleFetchResponse)
            .then(data => {
                if (data.status === 'success') {
                    document.querySelectorAll('.notification-item').forEach(item => {
                        item.remove();
                    });
                    updateNotificationCount(data.unread_count);
                } else {
                    console.error('Ошибка при пометке всех уведомлений как прочитанных:', data.message);
                    alert('Ошибка: ' + (data.message || 'Неизвестная ошибка.'));
                }
            })
            .catch(error => {
                console.error('Произошла ошибка сети или сервера при пометке всех уведомлений:', error);
                alert('Произошла ошибка: ' + error.message);
            });
        });
    }

document.addEventListener('DOMContentLoaded', function() {


    function updateNotificationCount(count) {
        const unreadCountElement = document.querySelector('.notification-count');
        if (unreadCountElement) {
            unreadCountElement.textContent = count;
            if (count === 0) {
                unreadCountElement.style.display = 'none';
            } else {
                unreadCountElement.style.display = 'inline-block';
            }
        }
    }

    function handleFetchResponse(response) {
        if (!response.ok) {
            return response.json().then(errorData => {
                throw new Error(errorData.message || `Server responded with status ${response.status}`);
            }).catch(() => {
                throw new Error(`Network response was not ok, status: ${response.status}`);
            });
        }
        return response.json();
    }


    if (typeof CSRF_TOKEN === 'undefined' || !CSRF_TOKEN) {
        console.error("CSRF_TOKEN is not defined or is empty. Please ensure it's set in your base.html.");
        return;
    }
    const csrfToken = CSRF_TOKEN;


    document.body.addEventListener('submit', function(event) {
        const form = event.target;
        if (form.classList.contains('js-friend-action-form')) {
            event.preventDefault();
            const formData = new FormData(form);
            const notificationItem = form.closest('.notification-item');

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(handleFetchResponse)
            .then(data => {
                if (data.status === 'success') {
                    if (notificationItem) {
                        notificationItem.classList.remove('unread');
                        const notificationActions = notificationItem.querySelector('.notification-actions');
                        if (notificationActions) {
                            notificationActions.style.display = 'none';
                        }
                    }
                    updateNotificationCount(data.unread_count);
                } else {
                    console.error('Ошибка в действии с запросом дружбы:', data.message);
                    alert('Ошибка: ' + (data.message || 'Неизвестная ошибка.'));
                }
            })
            .catch(error => {
                console.error('Произошла ошибка при отправке запроса дружбы:', error);
                alert('Произошла ошибка: ' + error.message);
            });
        }
    });

    document.body.addEventListener('click', function(event) {
        const deleteButton = event.target.closest('.close-notification-btn');

        if (deleteButton) {
            event.preventDefault();

            const notificationId = deleteButton.dataset.notificationId;
            const notificationItem = deleteButton.closest('.notification-item');

            if (!notificationId) {
                console.error('Notification ID not found for delete button. Check data-notification-id in HTML.');
                return;
            }

            fetch(`/profile/notifications/delete/${notificationId}/`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(handleFetchResponse)
            .then(data => {
                if (data.status === 'success') {
                    if (notificationItem) {
                        notificationItem.remove();
                    }
                    updateNotificationCount(data.unread_count);
                } else {
                    console.error('Ошибка удаления уведомления:', data.message);
                    alert('Ошибка удаления: ' + (data.message || 'Неизвестная ошибка.'));
                }
            })
            .catch(error => {
                console.error('Произошла ошибка сети или сервера при удалении уведомления:', error);
                alert('Произошла ошибка при удалении: ' + error.message);
            });
        }
    });
});