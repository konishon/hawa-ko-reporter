import sqlite3
from flask import Flask, request, make_response, jsonify, g
# from forecaster.solveathon_forecaster import *
from db import get_db, query_db


app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/hook', methods=['GET', 'POST'])
def index():
    with app.app_context():
        db = get_db(g)
        cur = db.cursor()
        event_type = "unsubscribe"

        if (event_type == "subscribe"):
            user_id = "1"
            platform = "viber"

            cur.execute(
                'INSERT INTO subs (user_id,platform,is_subscribed) values (?,?,?)',
                (
                    user_id,
                    platform,
                    True
                )
            )

            db.commit()
        elif(event_type == "unsubscribe"):

            user_id = "1"

            cur.execute(
                'UPDATE subs SET is_subscribed = ? WHERE user_id = ?',
                (
                    False,
                    user_id
                )
            )

            db.commit()

    return 'Hello World!'


def results():
    req = request.get_json(force=True)
    print(req)
    # fetch action from json
    intent_name = req.get('queryResult').get('intent').get('displayName')
    if(intent_name == "location"):
        print(intent_name)
        # pred = predict([0, 11, 'Sunday', 'Ratna'])
        return {'fulfillmentText': str("pred")}

    return {'fulfillmentText': 'This is a response from webhook.'}


@app.route('/aqi', methods=['GET', 'POST'])
def webhook():
    # return response
    print("AQI")
    return make_response(jsonify(results()))


if __name__ == '__main__':
    app.run()
