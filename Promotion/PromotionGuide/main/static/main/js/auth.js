document.addEventListener('DOMContentLoaded', function() {
    const navigationLinks1 = document.querySelectorAll('#registration');

    navigationLinks1.forEach(link => {
        link.addEventListener('click', function(e) {
            // Предотвращаем стандартное поведение клика
            e.preventDefault();

            // Отправляем AJAX-запрос на сервер
            fetch('registration', {
                method: 'GET',
                headers: {
                    'Content-Type': 'text/html'
                }
            })
           .then(response => response.text())
           .then(html => {
                // Заменяем содержимое страницы на полученный HTML-код
                document.querySelector('#body').innerHTML = html;
            })
           .catch(error => console.error('Error fetching content:', error));
        });
    });
});
