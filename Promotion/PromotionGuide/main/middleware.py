from datetime import timedelta
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from django.http import HttpResponseRedirect
import datetime

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Проверяем, существует ли атрибут 'session' в объекте 'request'
        if hasattr(request, 'session'):
            if 'last_activity' in request.session:
                session_expires = datetime.utcfromtimestamp(session_expires)
                current_time = timezone.now()
                time_difference = datetime.fromtimestamp(session_expires) - current_time
                if time_difference > timedelta(days=7):
                    # Удалить сессию, если она истекла
                    request.session.flush()
                    # Используйте HttpResponseRedirect для перенаправления
                    return HttpResponseRedirect('/')
                
    def process_response(self, request, response):
        if hasattr(request, 'session') and 'last_activity' in request.session:
            request.session['last_activity'] = timezone.now()
            expiry = timezone.now() + timedelta(days=7)
            request.session['expiry'] = expiry.total_seconds()
        return response
