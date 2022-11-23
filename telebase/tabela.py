import json

import pyrogram
import pyrogram.errors.exceptions as exceptions

from pyrogram.errors import FloodWait
from dicgram import Bot as DicBot


class Tabela:
    def __init__(self, seu_id: int, sua_base: int, gerenciador, app: pyrogram):
        self.seu_id = seu_id
        self.sua_base = sua_base
        self.gerenciador = gerenciador
        self.app = app
        self.g = None

    @staticmethod
    def criar_database(telebase):
        """
        Cria uma mensagem(db) gerenciadora
        """

        token = telebase.tokens if isinstance(telebase.tokens, str) else telebase.tokens[0]
        bot = DicBot(token=token, update=True)
        bot.comandos_publico['/start'] = telebase.start

    def drop_database(self):
        """
        Deleta a mensagem(db) gereciadora junto com todas as tabelas

        :return: None
        """

        self.g = self.gerenciador()
        for tabela in self.g['tabelas']:
            self.app().delete_messages(chat_id=self.seu_id, message_ids=self.g['tabelas'][tabela])
        self.app().delete_messages(chat_id=self.seu_id, message_ids=self.sua_base)

    def get_tabela(self, nome_tabela):
        """
        :return: Retorna a tabela
        """

        self.g = self.gerenciador()
        tabela = self.app().get_messages(chat_id=self.seu_id,
                                         message_ids=self.g['tabelas'][nome_tabela])
        c_i = tabela.text.find('{')
        c_f = tabela.text.rfind('}')
        tabela = json.loads(tabela.text[c_i:c_f + 1])

        return tabela

    def drop_tabela(self, nome_tabela):
        """
        :return: None
        """

        self.g = self.gerenciador()
        self.g['tabelas'].pop(nome_tabela)
        self.app().delete_messages(chat_id=self.seu_id, message_ids=self.g['tabelas'][nome_tabela])

        self.app().edit_message_text(chat_id=self.seu_id,
                                     message_id=self.sua_base,
                                     text=f'<b>TeleBase iniciado</b>\n\n'
                                          f'<code>{json.dumps(self.g, indent=2, ensure_ascii=False)}</code>\n\n'
                                          f'<i>Não apague esta mensagem!</i>')

    def add(self, nome_tabela, chave, valor):
        """
        Adiciona um valor a uma tabela
        :return: True se adicionado, False se não adicionado
        """

        tabela = self.get_tabela(nome_tabela)
        tabela['dados'][0][chave] = valor

        self.g = self.gerenciador()
        try:
            self.app().edit_message_text(chat_id=self.seu_id,
                                         message_id=self.g['tabelas'][nome_tabela],
                                         text=f'<code>{json.dumps(tabela, indent=2, ensure_ascii=False)}</code>')
            return True
        except FloodWait:
            self.app()
            self.add(nome_tabela, chave, valor)
        except exceptions.bad_request_400.MessageTooLong:
            return False

    def update(self, nome_tabela, chave, valor):
        """
        Atualiza um valor a uma tabela
        """

        self.add(nome_tabela, chave, valor)

    def get(self, nome_tabela, chave):
        """
        :return: Retorna o valor da chave
        """

        return self.get_tabela(nome_tabela)['dados'][0][chave]

    def get_all(self, nome_tabela):
        """
        :return: Retorna todos os valores da tabela
        """

        return self.get_tabela(nome_tabela)['dados'][0]

    def get_all_keys(self, nome_tabela):
        """
        :return: Retorna todas as chaves da tabela
        """

        return list(self.get_tabela(nome_tabela)['dados'][0].keys())

    def get_all_values(self, nome_tabela):
        """
        :return: Retorna todos os valores da tabela
        """

        return list(self.get_tabela(nome_tabela)['dados'][0].values())

    def delete(self, nome_tabela, chave):
        """
        Deleta um valor da tabela

        :return: True se deletado, False se não deletado
        """

        tabela = self.get_tabela(nome_tabela)
        if chave not in tabela['dados'][0]:
            return False
        tabela['dados'][0].pop(chave)

        self.g = self.gerenciador()
        try:
            self.app().edit_message_text(chat_id=self.seu_id,
                                         message_id=self.g['tabelas'][nome_tabela],
                                         text=f'<code>{json.dumps(tabela, indent=2, ensure_ascii=False)}</code>')
            return True
        except FloodWait:
            self.app()
            self.delete(nome_tabela, chave)
        except exceptions.bad_request_400.MessageTooLong:
            return False
