from flask import Flask,jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client =  MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
  'num_of_user':0
})
class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_user']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_user":new_num}})
        return str("User "+ str(new_num))

def checkPostedData(postedData, functionName):
    if(functionName == "add"or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

    elif(functionName == "divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #Resource add was requested using post
        postedData = request.get_json()
        stat = checkPostedData(postedData,"add")
        if(stat!=200):
            retJson = {
            "Message":"Error occured",
            "status code":stat
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
        "Message": ret,
        "status code" : 200
        }

        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        #Resource add was requested using post
        postedData = request.get_json()
        stat = checkPostedData(postedData,"subtract")
        if(stat!=200):
            retJson = {
            "Message":"Error occured",
            "status code":stat
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x-y
        retMap = {
        "Message": ret,
        "status code" : 200
        }

        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #Resource add was requested using post
        postedData = request.get_json()
        stat = checkPostedData(postedData,"multiply")
        if(stat!=200):
            retJson = {
            "Message":"Error occured",
            "status code":stat
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x*y
        retMap = {
        "Message": ret,
        "status code" : 200
        }

        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        #Resource add was requested using post
        postedData = request.get_json()
        stat = checkPostedData(postedData,"multiply")
        if(stat!=200):
            retJson = {
            "Message":"Error occured",
            "status code":stat
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = (x*1.0)/y
        retMap = {
        "Message": ret,
        "status code" : 200
        }

        return jsonify(retMap)



api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/divide")
api.add_resource(Visit,"/hello")




@app.route('/')
def hello_world():
    return "Hello World"

if __name__=="__main__":
    app.run(host ='0.0.0.0')
