import json
from flask import Flask
app = Flask(__name__)

data = {'message':'The air quality is great'}

data2 = {'message':'The air quality is imporving (reply from flask)'}

@app.route('/')
def hello():
    return json.dumps(data)

@app.route('/aqi', methods=['POST'])
def fetch_aqi():
    data = request.get_json(silent=True)
    print(data) 
    return json.dumps(data2)


if __name__ == '__main__':
    app.run(host='0.0.0.0')