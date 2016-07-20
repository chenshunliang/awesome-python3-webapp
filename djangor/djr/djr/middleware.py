from django.http import HttpResponse, JsonResponse


class LogMiddleware(object):
    def process_request(self, request):
        if request.method == 'POST':
            return HttpResponse(status=401)
        else:
            return JsonResponse({'log_info': '我被拦截啦'}, safe=False)
