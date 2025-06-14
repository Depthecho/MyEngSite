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

    document.getElementById('addAnother').addEventListener('click', function() {
        const form = document.querySelector('.card-form');
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'add_another';
        hiddenInput.value = '1';
        form.appendChild(hiddenInput);
        form.submit();
    });

    function flipMiniCard(element) {
        element.querySelector('.mini-card-inner').classList.toggle('flipped');
    }