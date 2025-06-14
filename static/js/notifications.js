document.addEventListener('DOMContentLoaded', function() {
    // Получение CSRF-токена.
    // Теперь он должен быть доступен либо через глобальную переменную globalCsrfToken,
    // либо через функцию getCookie, если она определена глобально (как в base.html).
    // Предпочтительнее использовать globalCsrfToken, если вы его установили.
    const csrfToken = typeof globalCsrfToken !== 'undefined' ? globalCsrfToken : getCookie('csrftoken');

    if (!csrfToken) {
        console.error("CSRF_TOKEN is not defined or is empty. Please ensure it's set in your base.html or a valid cookie exists.");
        // Можете добавить здесь более заметное сообщение или UI для пользователя
        return; // Прекращаем выполнение, если токена нет
    }

    // --- Элементы Навбара ---
    const avatarDropdown = document.getElementById('avatarDropdown');
    const dropdownMenu = document.getElementById('dropdownMenu');
    const notificationIcon = document.getElementById('notificationIcon');
    const notificationDropdown = document.getElementById('notificationDropdown');
    const burgerMenu = document.getElementById('burgerMenu');
    const navbarLinks = document.querySelector('.navbar-links');
    const navbarAuth = document.querySelector('.navbar-auth');
    const markAllReadBtn = document.getElementById('mark-all-read-btn');
    const notificationBadge = document.querySelector('.notification-badge'); // Элемент для счетчика уведомлений

    // --- Вспомогательные функции для уведомлений (из вашего notifications.js) ---
    function updateNotificationCount(count) {
        if (notificationBadge) {
            notificationBadge.textContent = count;
            if (count === 0) {
                notificationBadge.style.display = 'none';
            } else {
                notificationBadge.style.display = 'inline-block';
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

    // --- Логика закрытия всех выпадающих меню (из вашего inline-скрипта, улучшенная) ---
    function closeAllNavbarDropdowns(excludeElement = null) {
        if (dropdownMenu && dropdownMenu.style.display === 'block' && excludeElement !== avatarDropdown) {
            dropdownMenu.style.display = 'none';
        }
        if (notificationDropdown && notificationDropdown.style.display === 'block' && excludeElement !== notificationIcon) {
            notificationDropdown.style.display = 'none';
        }
        // Не закрываем бургер-меню здесь, оно имеет свою логику
    }

    // --- Обработчики событий Навбара (объединены) ---

    // Переключение выпадающего меню аватарки
    if (avatarDropdown) {
        avatarDropdown.addEventListener('click', (e) => {
            e.stopPropagation();
            const isMenuCurrentlyOpen = dropdownMenu.style.display === 'block';
            closeAllNavbarDropdowns(avatarDropdown); // Закрываем другие, если открыты
            dropdownMenu.style.display = isMenuCurrentlyOpen ? 'none' : 'block';
        });
    }

    // Переключение выпадающего меню уведомлений
    if (notificationIcon) {
        notificationIcon.addEventListener('click', (e) => {
            e.stopPropagation();
            const isMenuCurrentlyOpen = notificationDropdown.style.display === 'block';
            closeAllNavbarDropdowns(notificationIcon); // Закрываем другие, если открыты
            notificationDropdown.style.display = isMenuCurrentlyOpen ? 'none' : 'block';
        });
    }

    // Переключение бургер-меню
    if (burgerMenu) {
        burgerMenu.addEventListener('click', (e) => {
            e.stopPropagation();
            navbarLinks.classList.toggle('active');
            navbarAuth.classList.toggle('active');
            burgerMenu.classList.toggle('active');

            // При открытии бургер-меню, убедимся, что дропдауны закрыты
            if (navbarLinks.classList.contains('active')) {
                if (dropdownMenu) dropdownMenu.style.display = 'none';
                if (notificationDropdown) notificationDropdown.style.display = 'none';
            }
        });
    }

    // Глобальный слушатель кликов для закрытия выпадающих меню при клике вне их
    document.addEventListener('click', (e) => {
        // Закрываем дропдаун аватарки
        if (avatarDropdown && !avatarDropdown.contains(e.target) && !dropdownMenu.contains(e.target)) {
            dropdownMenu.style.display = 'none';
        }
        // Закрываем дропдаун уведомлений
        if (notificationIcon && !notificationIcon.contains(e.target) && !notificationDropdown.contains(e.target)) {
            notificationDropdown.style.display = 'none';
        }
        // Закрываем мобильное меню, если открыто и клик вне него
        if (burgerMenu && navbarLinks.classList.contains('active') && window.innerWidth <= 768 && !burgerMenu.contains(e.target) && !navbarLinks.contains(e.target) && !navbarAuth.contains(e.target)) {
            navbarLinks.classList.remove('active');
            navbarAuth.classList.remove('active');
            burgerMenu.classList.remove('active');
        }
    });

    // Обработка изменения размера окна для корректного отображения мобильного меню
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            if (navbarLinks) {
                navbarLinks.classList.remove('active');
                navbarLinks.style.display = ''; // Сброс стилей, если они были изменены классом .active
            }
            if (navbarAuth) {
                navbarAuth.classList.remove('active');
                navbarAuth.style.display = '';
            }
            if (burgerMenu) burgerMenu.classList.remove('active');
        }
    });

    // --- Логика Уведомлений (из вашего notifications.js) ---
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
                    // Удаляем все уведомления из списка (более надежно, чем remove())
                    const notificationList = document.querySelector('.notification-list');
                    if(notificationList) notificationList.innerHTML = '<div class="notification-empty"><p>No notifications yet</p></div>';

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