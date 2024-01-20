import requests

BASE_URL = "http://127.0.0.1:5000"


json_input = {
        "event" : "Daily standup",
        "coordinator" : "saddam",
        "date" : "2024-01-20",
        "start_time": "10:00",
        "end_time" : "11:00",
        "meeting_room" : "Room A",
        "attendee_list" : "[saddam]"
}

test = {
        "event" : "Daily standup"
}

# response = requests.get(BASE_URL + "/first/1")
# print("response : ", response.json())

input("Creating the event")
response = requests.post(BASE_URL + "/create_event", json =json_input)
print(response.json)