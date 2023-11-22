from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import DATABASE


def products_view(request):
    if request.method == "GET":
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ
