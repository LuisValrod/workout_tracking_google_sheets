from APP_ID_KEY import APP_ID, APP_KEY
import requests
from datetime import datetime

WEIGHT_KG = 87
HEIGHT_CM = 176
AGE = 36
GENDER = 'male'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/1c5b23146396cb65c6f420bc852f5579/workoutTracking/workouts'

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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": result["exercises"][0]["name"].title(),
#             "duration": result["exercises"][0]["duration_min"],
#             "calories": result["exercises"][0]["nf_calories"]
#         }
# }


sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

print(sheet_response.text)


