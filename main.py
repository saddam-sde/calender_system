from flask import Flask, request, jsonify
from flask_restful import Api, Resource, fields, marshal_with, reqparse, inputs
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
room_parser = reqparse.RequestParser()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'coordinator':fields.String,
    'date': fields.DateTime(dt_format='iso8601'),
    'start_time':fields.String,
    'end_time': fields.String,
    'meeting_room': fields.String,
    'attendee_list': fields.String
}

resource_fields_room = {
    'id': fields.Integer,
    'room_name': fields.String
}
parser.add_argument(
    'event',
    type=str,
    help='Topic of the meeting is required!',
    required=True
)

parser.add_argument(
    'coordinator',
    type=str,
    help='The Coordinator should be present!',
    required=True
)
parser.add_argument(
    'date',
    type=inputs.date,
    help='what is date of the meeting!',
    required=True
)

parser.add_argument(
    'start_time',
    type=str,
    help='time should be present',
    required=True
)

parser.add_argument(
    'end_time',
    type=str,
    help='time should be present',
    required=True
)

parser.add_argument(
    'meeting_room',
    type=str,
    help='time should be present',
    required=True
)

parser.add_argument(
    'attendee_list',
    type=str,
    help='time should be present',
    required=True
)

room_parser.add_argument(
    'room_name',
    type=str,
    help='Room should be present',
    required=True
)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String, nullable=False)
    coordinator = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    meeting_room = db.Column(db.String, nullable=False)
    attendee_list = db.Column(db.String)

class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String, nullable=False)

# with app.app_context():
#     db.create_all()

class RoomDetails(Resource):
    @marshal_with(resource_fields_room)
    def post(self):
        args = room_parser.parse_args()
        room_name = f"{args['room_name']}"
        room = Rooms(room_name = room_name)
        db.session.add(room)
        db.session.commit()
    
    @marshal_with(resource_fields_room)
    def get(self):
        result = Rooms.query.all()
        return result

#Get the event details
class EventDetails(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        print('id = ', id)
        result = Event.query.filter_by(id = id).first()
        return result
    
class Calender(Resource):
    
    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        event = f"{args['event']}" 
        coordinator = f"{args['coordinator']}"
        date = args['date'].date()
        start_time = f"{args['start_time']}"
        end_time = f"{args['end_time']}"
        meeting_room = f"{args['meeting_room']}"
        attendee_list = f"{args['attendee_list']}"

        new_event = Event(event = event, coordinator = coordinator, date = date, start_time = start_time, end_time= end_time, \
                          meeting_room = meeting_room, attendee_list = attendee_list)
        db.session.add(new_event)
        db.session.commit()

        return {"success"}

api.add_resource(Calender, '/create_event')
api.add_resource(EventDetails, '/Event/<int:id>')
api.add_resource(RoomDetails, '/Rooms')

if __name__ == "__main__":
    app.run(debug=True)
