#
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
#
#
parser =  reqparse.RequestParser()
parser.add_argument("info", type=str, help="information about given data")
parser.add_argument("size", type=int, help="size of the given data")
#
#
app = Flask(__name__)
api = Api(app)
#
#
points = {
    "p0" : {"x":3, "y":4, "z":5},
    "p1" : {"x":5, "y":12, "z":13},
    "p2" : {"x":8, "y":15, "z":17},
    "p3" : {"x":7, "y":24, "z":25},
    "p4" : {"x":20, "y":21, "z":29}
}
#
#
class testClass(Resource):
    """ 
    """
    def get(self, p):
        """ 
        """ 
        args = parser.parse_args()
        #
        if p in points:
            return {p : points[p]}, 400
        else:
            abort(404, message="Could not find video ...")
    #
    def post(self, p):
        """ 
        """ 
        return "ehe_post" + p + " = " + points[p]
    #
    def put(self, p):
        """ 
        """ 
        args = parser.parse_args()
        points[p] = args
        return points[p], 201
    #
    def delete(self, p):
        """ 
        """ 
        if p in points:
            del points[p]
            return 204
        else:
            abort(404, message="Could not find video ...")

    #
#
api.add_resource(testClass, "/test/<string:p>")
#
if __name__ == "__main__":
    app.run(debug=True)
#
#