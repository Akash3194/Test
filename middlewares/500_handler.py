from django.http import HttpResponse
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        return HttpResponse('Internal server error', content_type="application/json", status=500)

