document.addEventListener('DOMContentLoaded', function() {
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

        localStorage.setItem('sidebarState',
            sidebar.classList.contains('closed') ? 'closed' : 'open');
    }

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    }
    if (mobileSidebarToggle) {
        mobileSidebarToggle.addEventListener('click', toggleSidebar);
    }

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

    const closeInviteBtn = document.getElementById('closeInviteBtn');
    const inviteNotification = document.getElementById('inviteNotification');

    if (closeInviteBtn && inviteNotification) {
        closeInviteBtn.addEventListener('click', function() {
            inviteNotification.style.display = 'none';  //
        });
    }
});