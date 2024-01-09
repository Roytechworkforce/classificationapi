from flask_cors import CORS
from flask import Flask
from resources.Startup import Startup
from resources.database.db import db
from flask_restful import Api
app=Flask(__name__)
CORS(app)
api=Api(app)

UserNum=db["UserNum"]
UserNum.insert_one({"num_of_users":0})


api.add_resource(Startup,'/')

if __name__=='__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')