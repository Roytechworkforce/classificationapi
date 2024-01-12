from flask_cors import CORS
from flask import Flask
from resources.Startup import Startup
from resources.classify import Classify
from resources.register import Register,Refill
from flask_restful import Api
app=Flask(__name__)
CORS(app)
api=Api(app)

api.add_resource(Startup,'/')
api.add_resource(Register,'/register')
api.add_resource(Refill,'/refill')
api.add_resource(Classify,'/classify')
api

if __name__=='__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')