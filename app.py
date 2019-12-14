import sqlite3
from flask import Flask, request, make_response, jsonify, g
from db.sqlite_flask import get_db_for_flask,query_db
from db.sqlite import init_db
from messages.dialogflow import generate_dialog_flow_message
import json


app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/hook', methods=['GET', 'POST'])
def index():
    with app.app_context():
        db = get_db_for_flask(g)
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
    with app.app_context():

        db = get_db_for_flask(g)
        cur = db.cursor()

        req = request.get_json(force=True)
        pprint(req)
        intent_name = req.get('queryResult').get('intent').get('displayName')
        subscribe_to_daily_update = intent_name == "subscribe.upsell-yes"
        
        if(subscribe_to_daily_update):
            payload = req.get("originalDetectIntentRequest").get(
                "payload")

            user_profile = payload.get("data").get("userProfile")

            user_id = user_profile['id']
            platform = payload["source"]

            cur.execute(
                'INSERT INTO subs (user_id,platform,is_subscribed) values (?,?,?)',
                (
                    user_id,
                    platform,
                    True
                )
            )

            db.commit()
            return generate_dialog_flow_message("I will remind you daily :)")

        return {'fulfillmentText': 'This is a response from webhook.'}


@app.route('/aqi', methods=['GET', 'POST'])
def webhook():
    # return response
    print("AQI")
    return make_response(jsonify(results()))


def pprint(message):
    x = json.dumps(message, sort_keys=True, indent=4)
    print(x)


if __name__ == '__main__':
    init_db()

    app.run()
