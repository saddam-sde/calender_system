# calender_system
 This is a calender system application for managing and scheduling meeting and conferences.

MeetScheduler - Event Scheduling App
This is a simple event scheduling application built using Flask and SQLAlchemy. The app allows users to schedule events, check room availability, and manage room details.

Features
Create Event:

Endpoint: /create_event
Method: POST
Create a new event by providing the following parameters:
event (string): Topic of the meeting.
coordinator (string): Coordinator's name.
date (date): Date of the meeting (format: YYYY-MM-DD).
start_time (string): Start time of the meeting (format: HH:MM).
end_time (string): End time of the meeting (format: HH:MM).
meeting_room (string): Name of the meeting room.
attendee_list (string): List of attendees.
Get Event Details:

Endpoint: /Event (GET all events) or /Event/<int:id> (GET specific event by ID)
Method: GET
Retrieve details of all events or a specific event by providing its ID.
Room Management:

Endpoint: /Rooms
Method: POST (Add new room) or GET (Get all rooms)
Add a new meeting room or retrieve details of all meeting rooms.
Database
The application uses SQLite as its database, and the database file is named database.db. The database contains two tables:

Event Table:

Columns:
id (Integer): Event ID (Primary Key).
event (String): Topic of the meeting.
coordinator (String): Coordinator's name.
date (Date): Date of the meeting.
start_time (String): Start time of the meeting.
end_time (String): End time of the meeting.
meeting_room (String): Name of the meeting room.
attendee_list (String): List of attendees.
Rooms Table:

Columns:
id (Integer): Room ID (Primary Key).
room_name (String): Name of the meeting room.
Room Availability Check
The application checks room availability before scheduling a new event. It ensures that there are no scheduling conflicts for the specified meeting room, date, and time.

Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/meetscheduler.git
cd meetscheduler
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Access the application in your browser at http://127.0.0.1:5000.

Dependencies
Flask
Flask-RESTful
Flask-SQLAlchemy
Notes
Ensure that you have Python and pip installed on your system.
This application uses SQLite as the default database. You can modify the database URI in the app.py file if needed.
The application runs in debug mode (debug=True). Update this configuration for production deployment.
The application automatically creates the necessary database tables on startup (commented out in the current version).
This is a basic implementation, and additional features and enhancements can be added based on specific requirements.
Feel free to customize and extend the application as needed for your use case!