from flask import jsonify
from resources.database.db import db
from flask_restful import Resource
class Startup(Resource):
    def get(self):
        UserNum=db["UserNum"]
        prevNum=UserNum.find({})[0]['num_of_users']
        new_num=prevNum+1
        UserNum.update_one({},{'$set':{"num_of_users":new_num}})
        return jsonify({"Greetings":"Hello user "+str(new_num)})
    def post(self):
        return {"PostedData":"here is your posted data"}
