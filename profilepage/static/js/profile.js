document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const mobileSidebarToggle = document.getElementById('mobileSidebarToggle');

    const sidebarState = localStorage.getItem('sidebarState');
    if (sidebarState === 'closed') {
        sidebar.classList.add('closed');
        document.querySelector('.profile-container').classList.add('sidebar-closed');
    }

    function toggleSidebar() {
        sidebar.classList.toggle('closed');
        document.querySelector('.profile-container').classList.toggle('sidebar-closed');

        localStorage.setItem('sidebarState',
            sidebar.classList.contains('closed') ? 'closed' : 'open');
    }

    sidebarToggle?.addEventListener('click', toggleSidebar);
    mobileSidebarToggle?.addEventListener('click', toggleSidebar);

    document.getElementById('closeInviteBtn')?.addEventListener('click', function() {
        document.getElementById('inviteNotification').style.display = 'none';
    });
});