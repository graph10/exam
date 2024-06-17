document.addEventListener('DOMContentLoaded', function() {
    const filtersContainer = document.querySelector('.main-content_catalog_filters1');
    const arrow = filtersContainer.querySelector('.main-content_catalog_filters_arrow');
    const filtersHidden = document.querySelector('.main-content_catalog_filters-hidden1');

    let isFiltersVisible = false;

    // Обработчик события клика на стрелку
    arrow.addEventListener('click', function() {
        isFiltersVisible =!isFiltersVisible;
        if (isFiltersVisible) {
            filtersHidden.style.display = 'block';
        } else {
            filtersHidden.style.display = 'none';
        }
        arrow.classList.toggle('rotate-arrow');
    });

    // Обработчик события клика на контейнер фильтров
    filtersContainer.addEventListener('click', function(event) {
        // Предотвращаем всплытие события, чтобы не активировать другой обработчик
        event.stopPropagation();
        arrow.click(); // Симулируем клик по стрелке
    });

    // Функция для поворота стрелки
    function rotateArrow() {
        arrow.style.transform = isFiltersVisible? 'rotate(-90deg)' : 'rotate(0deg)';
    }
    
    // Добавление обработчика события для поворота стрелки
    arrow.addEventListener('click', rotateArrow);
});

document.addEventListener('DOMContentLoaded', function() {
    const filtersContainer = document.querySelector('.main-content_catalog_filters2');
    const arrow = filtersContainer.querySelector('.main-content_catalog_filters_arrow');
    const filtersHidden = document.querySelector('.main-content_catalog_filters-hidden2');

    let isFiltersVisible = false;

    // Обработчик события клика на стрелку
    arrow.addEventListener('click', function() {
        isFiltersVisible =!isFiltersVisible;
        if (isFiltersVisible) {
            filtersHidden.style.display = 'block';
        } else {
            filtersHidden.style.display = 'none';
        }
        arrow.classList.toggle('rotate-arrow');
    });

    // Обработчик события клика на контейнер фильтров
    filtersContainer.addEventListener('click', function(event) {
        // Предотвращаем всплытие события, чтобы не активировать другой обработчик
        event.stopPropagation();
        arrow.click(); // Симулируем клик по стрелке
    });

    // Функция для поворота стрелки
    function rotateArrow() {
        arrow.style.transform = isFiltersVisible? 'rotate(-90deg)' : 'rotate(0deg)';
    }
    
    // Добавление обработчика события для поворота стрелки
    arrow.addEventListener('click', rotateArrow);
});

document.addEventListener('DOMContentLoaded', function() {
    // Получаем все кнопки фильтров
    const filters = document.querySelectorAll('.main-content_catalog_filters-hidden1 button');
    let activeFilter = ''; // Переменная для хранения активного фильтра

    // Функция для обработки клика по фильтру
    function filterCards(filterValue) {
        // Находим все карточки
        const cards = document.querySelectorAll('.main-content_catalog-cards_card');

        // Если фильтр уже активен, сбрасываем его
        if (activeFilter === filterValue) {
            cards.forEach(card => card.style.display = 'flex'); // Показываем все карточки
            activeFilter = ''; // Сбрасываем активный фильтр
        } else {
            // Скрываем все карточки
            cards.forEach(card => card.style.display = 'none');

            // Показываем карточки, соответствующие выбранному фильтру
            cards.forEach(card => {
                const shopNameElement = card.querySelector('#shop');
                if (shopNameElement && shopNameElement.textContent.trim().toLowerCase().includes(filterValue)) {
                    card.style.display = 'flex';
                }
            });
            activeFilter = filterValue; // Обновляем активный фильтр
        }
    }

    // Обработчики событий для каждого фильтра
    filters.forEach(filter => {
        filter.addEventListener('click', function() {
            // Вызываем функцию фильтрации с значением фильтра
            filterCards(this.textContent.trim().toLowerCase());
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Получаем все кнопки фильтров
    const filters = document.querySelectorAll('.main-content_catalog_filters-hidden2 button');
    let activeFilter = ''; // Переменная для хранения активного фильтра

    // Функция для обработки клика по фильтру
    function filterCards(filterValue) {
        // Находим все карточки
        const cards = document.querySelectorAll('.main-content_catalog-cards_card');

        // Если фильтр уже активен, сбрасываем его
        if (activeFilter === filterValue) {
            cards.forEach(card => card.style.display = 'flex'); // Показываем все карточки
            activeFilter = ''; // Сбрасываем активный фильтр
        } else {
            // Скрываем все карточки
            cards.forEach(card => card.style.display = 'none');

            // Показываем карточки, соответствующие выбранному фильтру
            cards.forEach(card => {
                const shopNameElement = card.querySelector('#type');
                if (shopNameElement && shopNameElement.textContent.trim().toLowerCase().includes(filterValue)) {
                    card.style.display = 'flex';
                }
            });
            activeFilter = filterValue; // Обновляем активный фильтр
        }
    }

    // Обработчики событий для каждого фильтра
    filters.forEach(filter => {
        filter.addEventListener('click', function() {
            // Вызываем функцию фильтрации с значением фильтра
            filterCards(this.textContent.trim().toLowerCase());
        });
    });
});




