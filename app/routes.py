#########Import statement for the needed libraries and classes
from app import mongo
from flask import jsonify, make_response
from flask_restful import Resource
from app import api, app
from app.utils import mongo_data
import datetime
import uuid
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Generate(Resource):
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        payload = {
            "timestamp": datetime.datetime.now(),
            "uuid": str(uuid.uuid4())
        }
        mongo_data.insert_one(payload)
        output = mongo_data.find({}).sort("timestamp", -1)
        tobi = []
        for q in output:
            print({str(q['timestamp']): q['uuid']})
            tobi.append({str(q['timestamp']): q['uuid']})
        return jsonify(tobi)

  
# adding the defined resources along with their corresponding urls
api.add_resource(Generate, '/')