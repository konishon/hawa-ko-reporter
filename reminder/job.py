from messages.push_to_viber import message_to_viber
from db.sqlite import select_subs_by_platform

# from forecaster.solveathon_forecaster import predict

def messsage_viber_subscribers():
    subs = select_subs_by_platform("viber")
    for sub in subs:
        viber_id = sub[0]
        message_to_viber(viber_id,"a update from viber")
   
if __name__ == '__main__':
    messsage_viber_subscribers()