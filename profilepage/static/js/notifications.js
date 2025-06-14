document.addEventListener('DOMContentLoaded', function() {
    const avatarDropdown = document.getElementById('avatarDropdown');
    const dropdownMenu = document.getElementById('dropdownMenu');
    const notificationIcon = document.getElementById('notificationIcon');
    const notificationDropdown = document.getElementById('notificationDropdown');
    const burgerMenu = document.getElementById('burgerMenu');
    const navbarLinks = document.querySelector('.navbar-links');
    const navbarAuth = document.querySelector('.navbar-auth');

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

    window.closeNavbarDropdowns = closeAllNavbarDropdowns;
});