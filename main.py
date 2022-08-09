from keys import APP_ID, API_KEY,PASSWORD,USERNAME, BEARER_TOKEN, sheety_endpoint
import requests
import datetime as dt


exercise_query = input("What exercises did you do today?")
headers_parameters = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY

}
parameter_exercise = {
    "query": exercise_query,
    "gender": "female",
    "weight_kg": 61.5,
    "height_cm": 172,
    "age": 33
}
end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
r = requests.post(end_point, json=parameter_exercise, headers=headers_parameters)
r.raise_for_status()
data = r.json()
print(r.text)
print(len(data["exercises"]))
today_date = dt.datetime.now()
for i in range(0, len(data["exercises"])):
    print(data["exercises"][i]['name'])
    print(data)
    current_data = {
        "workout": {
            "date": str(today_date.date().strftime('%d/%m/%Y')),
            "time": today_date.strftime("%H:%M:%S"),
            "exercise": data["exercises"][i]['name'],
            "duration": data["exercises"][i]["duration_min"],
            "calories": data["exercises"][i]["nf_calories"]
        }
    }
    print(current_data)
    headers_sheety = {
        "Content-Type": "application/json"
    }

    # r = requests.post(sheety_endpoint, json =current_data, headers=headers_sheety, auth=(USERNAME, PASSWORD, ))
    # r.raise_for_status()
    bearer_headers = {
        "Authorization": "Bearer " + BEARER_TOKEN
    }
    r = requests.post(sheety_endpoint, json=current_data, headers=bearer_headers)
    r.raise_for_status()
