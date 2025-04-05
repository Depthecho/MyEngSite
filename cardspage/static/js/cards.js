document.addEventListener('DOMContentLoaded', function() {
    // Функция переворота карточки
    function flipCard(element) {
        element.classList.toggle('flipped');
    }

    // Обработчики для всех карточек
    const cards = document.querySelectorAll('.card-item');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            flipCard(this);
        });
    });

    // Переключение сайдбара
    const sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            document.getElementById('sidebar').classList.toggle('closed');
        });
    }
});