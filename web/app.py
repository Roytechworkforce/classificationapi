from flask_cors import CORS
from flask import Flask
from resources.Startup import Startup
from flask_restful import Api
app=Flask(__name__)
CORS(app)
api=Api(app)



api.add_resource(Startup,'/')

if __name__=='__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')