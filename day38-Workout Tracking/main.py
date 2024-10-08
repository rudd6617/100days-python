import requests
from datetime import datetime

APP_ID = "08314715"
API_KEY = "6c2644cf9b26ee1fbd57c76a1fece696"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/bcc0c17907b1b43958094ed5a9218f86/copyOfMyWorkouts/workouts"

SHEET_TOKEN = "KXCypt2ZOpyBtnxvhZNz7cfrQB8Tp9anQGs076oIrjImZpkAVvGb3wdxd8nw03yH"

exercise_text = input("What exercise are you doing? ")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-api-key": API_KEY,
}

# RUN 2 miles

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": "70",
    "height_cm": "180",
    "age": "30",
}

response = requests.post(EXERCISE_ENDPOINT, headers=exercise_headers, params=exercise_params)
# result = response.json()
print(response.text)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}",
}

for exercise in result["exercises"]:
    json_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    
    response = requests.post(SHEET_ENDPOINT, headers=sheet_headers, json=json_data)
    print(response.text)
  
  
# response = requests.get(SHEET_ENDPOINT)
# print(response.json())
    

# /v2/natural/nutrients

# https://trackapi.nutritionix.com/v2/natural/nutrients