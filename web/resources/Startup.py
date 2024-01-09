from flask import jsonify
from flask_restful import Resource
class Startup(Resource):
    def get(self):
        return jsonify({"Greetings":"Hey You've accessed Cassifcation API Send us your image We'll tell you what it is!"})
    def post(self):
        return {"PostedData":"here is your posted data"}
