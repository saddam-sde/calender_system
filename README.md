# calender_system
 This is a calender system application for managing and scheduling meeting and conferences.

# MeetScheduler - Event Scheduling App

MeetScheduler is a Flask-based event scheduling application that allows users to schedule events, check room availability, and manage room details.

## Features

1. **Create Event:**
   - Endpoint: `/create_event`
   - Method: POST
   - Create a new event by providing parameters such as `event`, `coordinator`, `date`, `start_time`, `end_time`, `meeting_room`, and `attendee_list`.

2. **Get Event Details:**
   - Endpoint: `/Event` (GET all events) or `/Event/<int:id>` (GET specific event by ID)
   - Method: GET
   - Retrieve details of all events or a specific event by providing its ID.

3. **Room Management:**
   - Endpoint: `/Rooms`
   - Method: POST (Add new room) or GET (Get all rooms)
   - Add a new meeting room or retrieve details of all meeting rooms.

## Database

The application uses SQLite as its database, and the database file is named `database.db`. The database contains two tables:

1. **Event Table:**
   - Columns: `id`, `event`, `coordinator`, `date`, `start_time`, `end_time`, `meeting_room`, `attendee_list`.

2. **Rooms Table:**
   - Columns: `id`, `room_name`.

## Room Availability Check

The application checks room availability before scheduling a new event, ensuring no conflicts for the specified meeting room, date, and time.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/meetscheduler.git
   cd meetscheduler

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

python main.py
