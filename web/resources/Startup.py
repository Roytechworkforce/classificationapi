from flask import jsonify
from resources.database.db import client
from flask_restful import Resource
db=client.aNewdb
UserNum=db["UserNum"]
UserNum.insert_one({"num_of_users":0})
class Startup(Resource):
    def get(self):
        UserNum=db["UserNum"]
        prevNum=UserNum.find({})[0]['num_of_users']
        new_num=prevNum+1
        UserNum.update_one({},{'$set':{"num_of_users":new_num}})
        return jsonify({"Greetings":"Hello zain "+str(new_num)})
    def post(self):
        return {"PostedData":"here is your posted data"}
