from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class helloWorld(Resource):
    def get(self, name=" ", age= 0):
        return {"data" : "Hello World",
                "method" : "GET",
                "name" : name,
                "age" : age
               }

    def post(self,name):
        return {"data" : "Hello World",
                "method" : "POST",
                "name" : name
               }

#api.add_resource(helloWorld, "/helloworld")
api.add_resource(helloWorld, "/helloworld/<string:name>/<int:age>")

if __name__ == "__main__" : 
    app.run(debug = True)