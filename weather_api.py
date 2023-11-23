import requests
from datetime import datetime

DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    token = '54d73608-c8dd-4c98-b18f-d9a5056525ab'
    url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}"
    headers = {"X-Yandex-API-Key": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    result = {
        # 'city': data['geo_object']['locality']['name'],
        # 'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
        'temp': data['fact']['temp'],
        'feels_like_temp': data['fact']['feels_like'],
        'pressure': data['fact']['pressure_mm'],
        'humidity': data['fact']['humidity'],
        'wind_speed': data['fact']['wind_speed'],
        'wind_gust': data['fact']['wind_gust'],
        # 'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
    }
    return result


# def current_weather(lat, lon):
#     """
#     Описание функции, входных и выходных переменных
#     """
#     token = 'b4588e45fcc14bdb89d63200232109'
#     url = f"https://api.weatherapi.com/v1/current.json?key={token}&q={lat},{lon}"
#     response = requests.get(url)
#     data = response.json()
#
#     result = {
#         'city': data['location']['name'],
#         'time': data['current']['last_updated'].split()[-1],
#         'temp': data['current']['temp_c'],
#         'feels_like_temp': data['current']['feelslike_c'],
#         'pressure': round(data['current']['pressure_mb'] * 0.75, 1),
#         'humidity': data['current']['humidity'],
#         'wind_speed': round(data['current']['wind_kph'] / 3.6, 1),
#         'wind_gust': round(data['current']['gust_kph'] / 3.6, 1),
#         'wind_dir': DIRECTION_TRANSFORM.get(data['current']['wind_dir'].lower()),
#     }
#     return result


if __name__ == "__main__":
    print(current_weather(59.93, 30.31))
