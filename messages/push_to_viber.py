from viberbot import Api
import os
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.viber_requests.viber_request import ViberRequest
from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage
)

bot_configuration = BotConfiguration(
    name='Hawa-ko-Reporter',
    avatar='http://viber.com/avatar.jpg',
    auth_token=os.environ['VIBER_AUTH_TOKEN']
)
viber = Api(bot_configuration)


def message_to_viber(viber_id, message):
    viber.send_messages(to=viber_id,
                        messages=[TextMessage(text=message)])
