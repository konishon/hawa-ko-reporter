import json
from flask import Flask
app = Flask(__name__)

data = {'message':'The air quality is great'}

data2 = {'message':'The air quality is imporving (reply from flask)'}

@app.route('/')
def fetch_aqi():
    return json.dumps(data2)

@app.route('/aqi', methods=['POST'])
def hello():
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')