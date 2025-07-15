document.addEventListener('DOMContentLoaded', function() {
    const avatarDropdown = document.getElementById('avatarDropdown');
    const dropdownMenu = document.getElementById('dropdownMenu');
    const notificationIcon = document.getElementById('notificationIcon');
    const notificationDropdown = document.getElementById('notificationDropdown');
    const burgerMenu = document.getElementById('burgerMenu');
    const navbarLinks = document.querySelector('.navbar-links');
    const navbarAuth = document.querySelector('.navbar-auth');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function closeAllNavbarDropdowns() {
        if (dropdownMenu) {
            dropdownMenu.style.display = 'none';
        }
        if (notificationDropdown) {
            notificationDropdown.style.display = 'none';
        }
        if (navbarLinks && navbarLinks.classList.contains('active')) {
            navbarLinks.classList.remove('active');
        }
        if (navbarAuth && navbarAuth.classList.contains('active')) {
             navbarAuth.classList.remove('active');
        }
    }

    if (avatarDropdown && dropdownMenu) {
        avatarDropdown.addEventListener('click', function(event) {
            event.stopPropagation();
            if (notificationDropdown && notificationDropdown.style.display === 'block') {
                notificationDropdown.style.display = 'none';
            }
            dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
        });
    }

    if (notificationIcon && notificationDropdown) {
        notificationIcon.addEventListener('click', function(event) {
            event.stopPropagation();
            if (dropdownMenu && dropdownMenu.style.display === 'block') {
                dropdownMenu.style.display = 'none';
            }
            notificationDropdown.style.display = notificationDropdown.style.display === 'block' ? 'none' : 'block';

            const markAllReadBtn = document.getElementById('mark-all-read-btn');
            if (markAllReadBtn) {
                fetch('/profile/notifications/mark_all_as_read/', {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        const unreadCountElement = document.getElementById('unreadNotificationCount');
                        if (unreadCountElement) {
                            unreadCountElement.style.display = 'none';
                            unreadCountElement.textContent = '0';
                        }
                        document.querySelectorAll('.notification-item.unread').forEach(item => {
                            item.classList.remove('unread');
                        });
                    }
                })
                .catch(error => console.error('Error marking all as read:', error));
            }
        });
    }

    if (burgerMenu) {
        burgerMenu.addEventListener('click', function(event) {
            event.stopPropagation();
            closeAllNavbarDropdowns();
            if (navbarLinks) {
                navbarLinks.classList.toggle('active');
            }
            if (navbarAuth) {
                navbarAuth.classList.toggle('active');
            }
        });
    }

    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            closeAllNavbarDropdowns();
        }
    });

    if (notificationDropdown) {
        notificationDropdown.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    }

    document.addEventListener('click', function(event) {
        if (dropdownMenu && event.target !== avatarDropdown && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
        if (notificationDropdown && event.target !== notificationIcon && !notificationDropdown.contains(event.target)) {
            notificationDropdown.style.display = 'none';
        }
        const isClickInsideBurgerMenu = burgerMenu.contains(event.target);
        const isClickInsideNavbarLinks = navbarLinks.contains(event.target);
        const isClickInsideNavbarAuth = navbarAuth.contains(event.target);

        if (!isClickInsideBurgerMenu && !isClickInsideNavbarLinks && !isClickInsideNavbarAuth) {
            if (navbarLinks) navbarLinks.classList.remove('active');
            if (navbarAuth) navbarAuth.classList.remove('active');
            if (burgerMenu) burgerMenu.classList.remove('active');
        }
    });

    const notificationListContainer = document.querySelector('.notification-list');

    if (notificationListContainer) {
        notificationListContainer.addEventListener('click', function(event) {
            const deleteBtn = event.target.closest('.close-notification-btn');
            if (deleteBtn) {
                event.stopPropagation();
                const notificationItem = deleteBtn.closest('.notification-item');
                const notificationId = deleteBtn.dataset.notificationId;

                if (notificationId && notificationItem) {
                    fetch(`/profile/notifications/delete/${notificationId}/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            notificationItem.remove()

                            const unreadCountElement = document.getElementById('unreadNotificationCount');
                            if (unreadCountElement) {
                                unreadCountElement.textContent = data.unread_count;
                                if (data.unread_count === 0) {
                                    unreadCountElement.style.display = 'none';
                                } else {
                                    unreadCountElement.style.display = 'block';
                                }
                            }
                        } else {
                            console.error('Error deleting notification:', data.message);
                        }
                    })
                    .catch(error => console.error('Error:', error));
                }
            }
        });
    }

    const markAllReadBtn = document.getElementById('mark-all-read-btn');
    if (markAllReadBtn) {
        markAllReadBtn.addEventListener('click', function(event) {
            event.preventDefault();
            fetch('/profile/notifications/mark_all_as_read/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const unreadCountElement = document.getElementById('unreadNotificationCount');
                    if (unreadCountElement) {
                        unreadCountElement.style.display = 'none';
                        unreadCountElement.textContent = '0';
                    }
                    document.querySelectorAll('.notification-item.unread').forEach(item => {
                        item.classList.remove('unread');
                    });
                    messages.success(request, "All notifications marked as read.");
                } else {
                    console.error('Error marking all as read:', data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});