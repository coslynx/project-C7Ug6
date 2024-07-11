import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models.manhwa_model import Manhwa

@csrf_exempt
def get_manhwas(request):
    manhwas = Manhwa.objects.all()
    data = [{"title": manhwa.title, "author": manhwa.author, "genre": manhwa.genre} for manhwa in manhwas]
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_manhwa(request, manhwa_id):
    try:
        manhwa = Manhwa.objects.get(id=manhwa_id)
        data = {"title": manhwa.title, "author": manhwa.author, "genre": manhwa.genre}
        return JsonResponse(data)
    except Manhwa.DoesNotExist:
        return JsonResponse({"error": "Manhwa not found"}, status=404)

@csrf_exempt
def create_manhwa(request):
    data = json.loads(request.body)
    title = data.get("title", "")
    author = data.get("author", "")
    genre = data.get("genre", "")

    if title and author and genre:
        manhwa = Manhwa.objects.create(title=title, author=author, genre=genre)
        return JsonResponse({"message": "Manhwa created successfully"}, status=201)
    else:
        return JsonResponse({"error": "Missing required fields"}, status=400)

@csrf_exempt
def update_manhwa(request, manhwa_id):
    try:
        manhwa = Manhwa.objects.get(id=manhwa_id)
        data = json.loads(request.body)
        title = data.get("title", manhwa.title)
        author = data.get("author", manhwa.author)
        genre = data.get("genre", manhwa.genre)

        manhwa.title = title
        manhwa.author = author
        manhwa.genre = genre
        manhwa.save()

        return JsonResponse({"message": "Manhwa updated successfully"})
    except Manhwa.DoesNotExist:
        return JsonResponse({"error": "Manhwa not found"}, status=404)

@csrf_exempt
def delete_manhwa(request, manhwa_id):
    try:
        manhwa = Manhwa.objects.get(id=manhwa_id)
        manhwa.delete()
        return JsonResponse({"message": "Manhwa deleted successfully"})
    except Manhwa.DoesNotExist:
        return JsonResponse({"error": "Manhwa not found"}, status=404)