# import flask dependencies
from flask import Flask, request, make_response, jsonify
from forecaster.solveathon_forecaster import *

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

def results():
    # build a request object
    req = request.get_json(force=True)
    
    
    # fetch action from json
    intent_name = req.get('queryResult').get('intent').get('displayName')
    if(intent_name=="location"):
        print(intent_name)
        pred = predict([0, 11, 'Sunday', 'Ratna'])
        return {'fulfillmentText': str(pred)}
  


   
    return {'fulfillmentText': 'This is a response from webhook.'}

@app.route('/aqi', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()