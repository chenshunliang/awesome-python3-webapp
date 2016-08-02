from django.http import HttpResponse, JsonResponse
import logging


class LogMiddleware(object):
    def process_request(self, request):
        if request.method == 'POST':
            return HttpResponse(status=401)
        else:
            return JsonResponse({'log_info': '我被拦截啦'}, safe=False)


class ErrorLogMiddware(object):
    def process_exception(self, request, exception):
        import logging
        logger = logging.getLogger('django')  # 这里用__name__通用,自动检测.
        logger.info('异常捕获')
        return HttpResponse(dir(exception))
