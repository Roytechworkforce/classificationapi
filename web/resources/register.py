from flask_restful import  Resource
from flask import jsonify,request
from resources.database.db import client
import bcrypt
db=client.ImageRecognition
users=db["Users"]

def UserExist(username):
    if users.count_documents({"Username":username})==0:
        return False
    else:
         return True

class Register(Resource):
    def post(self):
        postedData=request.get_json()

        username=postedData["username"]
        password=postedData["password"]
        if UserExist(username):
            retJson={
                "status":301,
                "msg":"Invalid Username"
            }
            return jsonify(retJson)
        hashed_pw=bcrypt.hashpw(password.encode("utf8"),bcrypt.gensalt())

        users.insert_one({
            "Username":username,
            "Password":hashed_pw,
            "Tokens":4
        })
        retJson={
            "status":200,
            "msg":"You're registered"
        }
        return jsonify(retJson)
class Refill(Resource):
    def post(self):
        postedDATA=request.get_json()
        username=postedDATA["username"]
        password=postedDATA["admin_pw"]
        amount=postedDATA["amount"]
        if not UserExist(username):
            return jsonify({
                "status":301,
                "msg":"Invalid Username"
            })
        correct_pw="abc123"
        if not password==correct_pw:
            return jsonify({
                "status":304,
                "msg":"Invalid Amin Password"
            })
        users.update_one({
            "Username":username
        },{
            "$set":{
                "Tokens":amount
            }
        })
        return jsonify({
            "status":200,
            "msg":"Refilled"
        })