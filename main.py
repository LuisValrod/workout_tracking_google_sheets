import requests
from datetime import datetime
import os

WEIGHT_KG = 87
HEIGHT_CM = 176
AGE = 36
GENDER = 'male'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.environ['NT_SHEETY_ENDPOINT']
# sheety_endpoint = 'https://api.sheety.co/1c5b23146396cb65c6f420bc852f5579/workoutTracking/workouts'

headers = {
    'x-app-id': os.environ["NT_APP_ID"],
    'x-app-key': os.environ["NT_APP_KEY"]
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

# Basic Authentication
'''

sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=(os.environ['NT_USERNAME'], os.environ['NT_PASSWORD']))

'''

# Bearer Token Authentication

token = os.environ['NT_TOKEN']
headers = {"Authorization": f"Bearer {token}"}

sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=headers)




# sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

print(sheet_response.text)



# References for authentication

'''
https://sheety.co/docs/authentication.html
https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication


'''

