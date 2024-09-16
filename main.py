from APP_ID_KEY import APP_ID, APP_KEY
import requests

WEIGHT_KG = 87
HEIGHT_CM = 176
AGE = 36
GENDER = 'male'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}


exercise_input = input('Tell me what exercise you did: \n')

parameters = {
    'query': exercise_input,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
    'gender': GENDER
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)



