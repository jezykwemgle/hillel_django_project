from triangle.models import LogEntry


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin'):
            method = request.method
            path = request.path
            query = request.GET.dict()
            body = request.POST.dict()
            data = {
                'method': method,
                'path': path,
                'query': query,
                'body': body,
            }
            LogEntry.objects.create(path=path, method=method, request_data=data)
        response = self.get_response(request)
        return response
