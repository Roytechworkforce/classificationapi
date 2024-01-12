from flask_restful import Resource
from resources.database.db import client
from flask import jsonify,request
import requests
import os
import subprocess
import json
import bcrypt

db=client.ImageRecognition
users=db["Users"]

def genrateReturn(status,comment):
    retJson={
        "status":status,
        "msg":comment
    }
    return retJson
def UserExist(username):
    if users.count_documents({"Username":username})==0:
        return False
    else:
         return True
def verify_pw(username,password):
    if not UserExist(username):
        return False
    hashed_pw=users.find({
        "Username":username
    })[0]["Password"]
    if bcrypt.hashpw(password.encode('utf8'),hashed_pw)==hashed_pw:
        return True
    else:
        return False
    return
def verify_crediantials(username,password):
    if not UserExist(username):
        print("Checking Username")
        return genrateReturn(301,"Invalid User"),True
    correct_pw=verify_pw(username,password)
    if not correct_pw:
        print("Checking Password")
        return genrateReturn(302,"Invalid Password"),True
    return None,False
class Classify(Resource):
    def post(self):
        posted_data=request.get_json()
        username=posted_data["username"]
        password=posted_data["password"]
        url=posted_data["url"]
        retJson,error=verify_crediantials(username,password)
        if error:
            return jsonify(retJson)
        tokens=users.find({
            "Username":username
        })[0]["Tokens"]
        print(tokens)
        if tokens<=0:
            return jsonify(genrateReturn(303,"Not Enough tOKENS"))
        r=requests.get(url)
        retJson={}
        with open("temp.jpg","wb") as f:
            f.write(r.content)
            proc=subprocess.Popen('python classify_image.py --model_dir=. --image_file=./temp.jpg',shell=False if os.name=='nt' else True)
            proc.communicate()[0]
            proc.wait()
            with open("text.txt") as g:
                retJson=json.load(g)
        users.update_one({
            "Username":username
        },{"$set":{
            "Tokens":tokens-1
        }})
        return retJson