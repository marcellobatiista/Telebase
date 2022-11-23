import json
import sys


class Gerenciador:

    bots = []
    atual = 0

    def __init__(self, seu_id: int, sua_base: int):
        self.seu_id = seu_id
        self.sua_base = sua_base

    def app(self):
        """
        Toda vez que for usar o app,
        ele vai pegar o próximo bot da lista

        :return: Retorna o bot atual
        """

        self.atual = (self.atual + 1) % len(self.bots)
        return self.bots[self.atual]

    def gerenciador(self):
        """
        :return: Retorna a mensagem gerenciadora de tabelas
        """

        mg = self.app().get_messages(chat_id=self.seu_id, message_ids=self.sua_base)
        c_i = mg.text.find('{')
        c_f = mg.text.rfind('}')
        mg = json.loads(mg.text[c_i:c_f + 1])

        return mg

    @staticmethod
    def start(mim, msg, args):
        if not args:
            return 'Olá, seja bem vindo ao DBot, o bot que te ajuda a gerenciar seus dados. ' \
                   'Para iniciar digite /start db\n'
        elif args[0] == 'db':
            init = mim.send_message(chat_id=msg.chat.id, text='Iniciando...')

            g = json.dumps({
                'ID': msg.chat.id,
                'base': init.message_id,
                'tabelas': {}
            }, indent=2, ensure_ascii=False)

            mim.edit_message_text(chat_id=msg.chat.id,
                                  message_id=init.message_id,
                                  text=f'<b>TeleBase iniciado</b>\n\n'
                                       f'<code>{g}</code>\n\n'
                                       f'<i>____</i>',
                                  parse_mode='HTML')
            sys.exit()
