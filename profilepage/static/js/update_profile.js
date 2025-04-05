document.addEventListener('DOMContentLoaded', function() {
    window.scrollTo(0, 0);

    const editProfileButton = document.querySelector('a[href*="update_profile"]');
    if (editProfileButton) {
        editProfileButton.addEventListener('click', function(e) {
            e.preventDefault();
            sessionStorage.setItem('scrollPosition', window.scrollY);
            window.location.href = this.href;
        });
    }

    const scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition) {
        setTimeout(() => {
            window.scrollTo(0, 0);
            sessionStorage.removeItem('scrollPosition');
        }, 0);
    }

    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const mobileSidebarToggle = document.getElementById('mobileSidebarToggle');
    const updateProfileContainer = document.querySelector('.update-profile-container');

    const sidebarState = localStorage.getItem('sidebarState');
    if (sidebarState === 'closed') {
        sidebar.classList.add('closed');
        updateProfileContainer.classList.add('sidebar-closed');
    }

    function toggleSidebar() {
        sidebar.classList.toggle('closed');
        updateProfileContainer.classList.toggle('sidebar-closed');
        localStorage.setItem('sidebarState', sidebar.classList.contains('closed') ? 'closed' : 'open');
    }

    sidebarToggle?.addEventListener('click', toggleSidebar);
    mobileSidebarToggle?.addEventListener('click', toggleSidebar);

    const avatarInput = document.getElementById('id_avatar');
    const avatarImg = document.querySelector('.update-avatar-img');

    if (avatarInput && avatarImg) {
        avatarInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    avatarImg.src = event.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }
});