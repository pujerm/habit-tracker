import requests
from datetime import datetime

USERNAME = "your_username"
TOKEN =  "your_token"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graphs_params = {
    "id": GRAPH_ID,
    "name": "Python learning",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
    "timezone": ""
}

headers ={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graphs_params, headers=headers)
# print(response.text)

today = datetime(year=2023, month=9,day=1)
# print(today.strftime("%Y%m%d"))

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "140"
}

pixel_endpoint_post = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

# response = requests.post(url= pixel_endpoint_post, json=post_pixel_params, headers=headers)
# print(response.text)

day_to_change = "20230902"
numbers_of_minutes = "135"

to_change_pixel = f"{pixel_endpoint_post}/{day_to_change}"

change_pixel_params = {
    "quantity" : numbers_of_minutes
}

# response = requests.put(url = to_change_pixel, json=change_pixel_params, headers=headers)
# print(response.text)


# response = requests.delete(url = to_change_pixel, headers=headers)
# print(response.text)
