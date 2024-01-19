from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class calender(Resource):
    def get(self):
        return {'data':'Hello'}

api.add_resource(calender, '/first')

if __name__ == "__main__":
    app.run(debug=True)
