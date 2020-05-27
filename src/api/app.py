from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class IdeaParkingLot(Resource):
    def get(self):
        return {'hello': 'cloud gurus'}


api.add_resource(IdeaParkingLot, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
