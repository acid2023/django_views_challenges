"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest
import lorem

def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    length = int(request.GET.get('length', False))
    if not length or length > 1000:
        return HttpResponse(status=403)
    text = lorem.text()[:length]
    response = HttpResponse(
        text,
        content_type='text/plain',
        headers={'Content-Disposition': 'attachment; filename="lorem.txt"'},)
    return response

