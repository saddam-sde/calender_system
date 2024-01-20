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

room = {
        "room_name" : "Room A"
}

"""Get Event Details"""
response = requests.get(BASE_URL + "/Event/1")
print("response : ", response.json())

input("Room List")
response = requests.get(BASE_URL + "/Rooms")
print("response : ", response.json())

# input('Adding Room A in the room db')
# response = requests.post(BASE_URL + "/Rooms", json =room)
# print(response.json)

input("Creating the event")
"""Conflicting unit test"""
response = requests.post(BASE_URL + "/create_event", json =json_input)
print(response.json)

"""[datetime.date(2024, 1, 20)]
Meeting room is not avialable"""