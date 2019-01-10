from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
  if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
    if "x" not in postedData or "y" not in postedData:
      return 301
    else:
      return 200

  if (functionName == "divide"):
    if "x" not in postedData or "y" not in postedData:
      return 301
    elif int(postedData["y"])==0:
      return 302
    else:
      return 200
    


class Add(Resource):
  def post(self):
    #If I am here, then the resource Add was requested using the method POST

    postedData = request.get_json()

    status_code = checkPostedData(postedData, "add")
    if(status_code!=200):
      retJson = {
        "Message": "An error occurred: Bad Input",
        "Status Code": status_code
      }
      return jsonify(retJson)

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)

    ret = x+y
    retMap = {
      'Message':ret,
      'Status Code':status_code
    }
    return jsonify(retMap)

class Subtract(Resource):
  def post(self):
    #If I am here, then the resource Subtract was requested using the method POST

    postedData = request.get_json()

    status_code = checkPostedData(postedData, "subtract")
    if(status_code!=200):
      retJson = {
        "Message": "An error occurred: Bad Input",
        "Status Code": status_code
      }
      return jsonify(retJson)

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)

    ret = x-y
    retMap = {
      'Message':ret,
      'Status Code':status_code
    }
    return jsonify(retMap)


class Multiply(Resource):
  def post(self):
    #If I am here, then the resource Multiply was requested using the method POST

    postedData = request.get_json()

    status_code = checkPostedData(postedData, "multiply")
    if(status_code!=200):
      retJson = {
        "Message": "An error occurred: Bad Input",
        "Status Code": status_code
      }
      return jsonify(retJson)

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)

    ret = x*y
    retMap = {
      'Message':ret,
      'Status Code':status_code
    }
    return jsonify(retMap)

class Divide(Resource):
  def post(self):
    #If I am here, then the resource Divide was requested using the method POST

    postedData = request.get_json()

    status_code = checkPostedData(postedData, "divide")
    if(status_code!=200):
      retJson = {
        "Message": "An error occurred: Bad Input",
        "Status Code": status_code
      }
      return jsonify(retJson)

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)

    ret = x/y
    retMap = {
      'Message':ret,
      'Status Code':status_code
    }
    return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
  return "You hit a custom url from Flask!"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
  # Get x,y from posted data
  dataDict = request.get_json()

  if "x" not in dataDict:
    return "ERROR", 305
  if "y" not in dataDict:
    return "ERROR", 305

  # Add
  z = dataDict["x"] + dataDict["y"]

  # Prepare a JSON, "z":z
  retJSON = {
    "z":z
  }

  # Return JSON and 200 OK code
  return jsonify(retJSON), 200

@app.route('/bye')
def bye():
  retJson = {
    'Name':'Tom',
    'Age':24,
    'phones':[
      {
          "phoneName":"PixelXL",
          "phoneNumber":"111-222-3333"
      },
      {
          "phoneName":"Google Voice",
          "phoneNumber":"444-555-6666"
      }
    ]
  }
  #return "Goodbye"
  return jsonify(retJson)

if __name__=="__main__":
  app.run(host='0.0.0.0', port='5000', debug=True)
