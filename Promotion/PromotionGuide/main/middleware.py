from datetime import timedelta
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from django.http import HttpResponseRedirect

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Проверяем, существует ли атрибут 'session' в объекте 'request'
        if hasattr(request, 'session'):
            if 'last_activity' in request.session:
                session_expires = request.session.get_decoded().get('expiry')
                current_time = timezone.now()
                time_difference = session_expires - current_time
                if time_difference <= timedelta(days=7):
                    # Удалить сессию, если она истекла
                    request.session.flush()
                    # Используйте HttpResponseRedirect для перенаправления
                    return HttpResponseRedirect('/')
