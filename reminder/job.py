from messages.push_to_viber import message_to_viber
from db.sqlite import select_subs_by_platform

# from forecaster.solveathon_forecaster import predict

def messsage_viber_subscribers(message):
    subs = select_subs_by_platform("viber")
    print("[INFO] messaging {0} people".format(len(subs)))
    for sub in subs:
        viber_id = sub[0]
        message_to_viber(viber_id,message)
   
if __name__ == '__main__':
    messsage_viber_subscribers()