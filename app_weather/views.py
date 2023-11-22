from django.shortcuts import render
from django.http import JsonResponse
from weather_api import current_weather


def weather_view(request):
    if request.method == "GET":
        data = current_weather(59.93, 30.31)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})
