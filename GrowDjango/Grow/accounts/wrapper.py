from functools import wraps
from django.http import HttpResponseBadRequest, JsonResponse
import logging


def require_header(header_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            logging.info(
                "Request Url: " + str(request.get_host() + request.get_full_path()) + "\nRequest method: " + str(
                    request.method)
                + "\nRequest headers:" + str(request.headers))
            if request.method == 'OPTIONS':

                if header_name not in request.headers:
                    return HttpResponseBadRequest("Missing required header: " + header_name)
                elif header_name != 'MY0lPlYlApNZmlbt':
                    return HttpResponseBadRequest("Unauthorized Access！")
                return view_func(request, *args, **kwargs)
            else:
                return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator


def handle_exceptions(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            response = view_func(request, *args, **kwargs)
        except Exception as e:
            response = JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
        return response

    return wrapper