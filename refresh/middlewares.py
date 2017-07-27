from .models import *
from datetime import datetime


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        date = datetime.now()
        url = request.get_full_path()
        Refresh.objects.get_or_create(url=url, ip=ip, datetime=date)

        instant_t = date.replace(minute=date.minute-1)
        refreshes = Refresh.objects.filter(datetime__gte=instant_t)
        refresh_len = len(refreshes)

        response.context_data["refresh"] = refresh_len


        # Code to be executed for each request/response after
        # the view is called.

        return response
