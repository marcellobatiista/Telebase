import random

from pyrogram import Client, enums


class Bot:
    def __init__(self, token):
        self.token = token
        self.cliente = Bot.criar_cliente(token)

    @staticmethod
    def criar_cliente(token):
        """
        :param token: Token do seu bot
        :return: Cliente do seu bot
        """

        return Client(name=str(random.randint(1, 100)),
                      bot_token=token,
                      no_updates=True,
                      in_memory=True,
                      api_id=19189289,
                      api_hash='d68ff633ae3d8239d0f50105eba6eb77',
                      parse_mode=enums.ParseMode.HTML)
