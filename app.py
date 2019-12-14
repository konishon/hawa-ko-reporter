# import flask dependencies
from flask import Flask, request, make_response, jsonify
from forecaster.solveathon_forecaster import *

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello Nishon!'

def results():
    # build a request object
    req = request.get_json(force=True)
    print(req)

    

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}

@app.route('/aqi', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()