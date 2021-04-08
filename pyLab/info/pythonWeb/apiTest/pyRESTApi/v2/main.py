from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"furkanIbnesi" :{"name":"furkanIbnesi", "age" : 18, "gender" : "citir"},
         "fatihGayi" : {"age" : 21, "gender" : "gay"}
        }

class helloWorld(Resource):
    def get(self, name=" ", age= 0):
        return names[name]

    def post(self,name):
        return {"data" : "Hello World",
                "method" : "POST",
                "name" : name
               }

#api.add_resource(helloWorld, "/helloworld")
api.add_resource(helloWorld, "/helloworld/<string:name>")

if __name__ == "__main__" : 
    app.run(debug = True)