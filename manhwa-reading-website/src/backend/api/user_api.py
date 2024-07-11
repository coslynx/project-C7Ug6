import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models.user_model import User

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'message': 'Username already exists'}, status=400)
            else:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                
                return JsonResponse({'message': 'User registered successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = User.objects.get(username=username)
            
            if user.check_password(password):
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            user = User.objects.get(id=user_id)
            
            new_username = request.POST.get('new_username')
            new_email = request.POST.get('new_email')
            
            if new_username:
                user.username = new_username
            if new_email:
                user.email = new_email
                
            user.save()
            
            return JsonResponse({'message': 'User updated successfully'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)