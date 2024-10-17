import requests
import strftime

PIXELA_ENDPOINT = "https://pixe.la"
PIXELA_TOKEN = "______YOUR_PIXELA_TOKEN_____"
PIXELA_USERNAME = "rudd"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=f"{PIXELA_ENDPOINT}/v1/users", json=user_params)
# print(response.json())


headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_params = {
    "id": "graph-1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

response = requests.post(url=f"{PIXELA_ENDPOINT}/v1/users/{PIXELA_USERNAME}/graphs", json=graph_params, headers=headers)
print(response.text)

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))