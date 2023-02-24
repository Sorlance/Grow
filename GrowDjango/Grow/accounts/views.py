from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from .wrapper import require_header, handle_exceptions


# Create your views here.
@csrf_exempt
@handle_exceptions
@require_header('Authorization')
def register_user(request):
    if request.method == 'POST':
        # 解析 POST 请求中的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 在数据库中创建新用户
        try:
            user = User.objects.create_user(username, None, password)
            user.save()
            return JsonResponse({'status': 'success'})
        except HttpResponseBadRequest as e:
            raise Exception(e.message)
        except Exception as e:
            raise Exception("Create user failed")
    else:
        raise Exception("Use POST")
