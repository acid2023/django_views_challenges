"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""

from django.http import HttpResponse, HttpRequest
import json
import re

def get_json_data(request: HttpRequest) -> tuple[bool, dict[str, str] | None]:
    if request.method == 'POST' or request.method == 'GET':
        try:
            data = json.loads(request.body)
            return True, data
        except json.JSONDecodeError:
            return False, None
    else:
        return False, None

def check_email_format(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_full_name_format(full_name: str) -> bool:
    pattern = r'^[a-zA-Zа-яА-ЯёЁ]{5,256}$'
    return re.match(pattern, full_name) is not None

def check_registered_from_format(registered_from: str) -> bool:
    return registered_from in ['website', 'mobile_app']

def check_age_format(age: str) -> bool:
    return age.isdigit()

def check_headers(json_date: dict[str, str]) -> bool:
    valid_headers = ['full_name', 'email', 'registered_from']
    actual_headers = list(json_date.keys())
    print(actual_headers)

    for header in valid_headers:
        if header not in actual_headers:
            return False

    for header in actual_headers:
        if header not in valid_headers and header != 'age':
            return False
    return True

def check_json(json_data: dict[str, str]) -> bool:
    if not check_headers(json_data):
        return False
    if not check_full_name_format(json_data['full_name']):
        return False
    if not check_email_format(json_data['email']):
        return False
    if not check_registered_from_format(json_data['registered_from']):
        return False
    if 'age' in list(json_data.keys()):
        if not check_age_format(json_data['age']):
            return False 
    return True

def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    json_check, json_data = get_json_data(request)
    
    if not json_check:
        return HttpResponse({"error": "Bad Request"}, status=400)
   
    if check_json(json_data):
        return HttpResponse({"is_valid": True}, status=200)
    else:
        return HttpResponse({"is_valid": False}, status=200)

