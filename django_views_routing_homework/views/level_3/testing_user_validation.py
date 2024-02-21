import json
from django.utils.http import urlencode

'''
Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

'''




import requests
import json

# URL to which the request will be sent
url = 'http://127.0.0.1:8000/user/validate/'

data = {
    "full_name": "valueA",
    "email": "value2@value2.com",
    "registered_from": "mobile_app",
    "age": '5',
   # "somethin" : '5'
}

# Convert the JSON object to a string
json_data = json.dumps(data)
encoded_json_data = urlencode({'json_data': json_data})


# Send a POST request with JSON data
response = requests.post(url, json=data)

# Check the status code
if response.status_code == 200:
    print(response.json())


else:
    # If the status code is not 200, print the error message
    print(f"Request failed with status code {response.json()}: {response.content}")