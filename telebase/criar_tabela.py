import json
import time

from pyrogram.errors import FloodWait


class CriarTabela:
    def __init__(self, nome_tabela, seu_id, sua_base, gerenciador, app):
        self.nome_tabela = nome_tabela
        self.seu_id = seu_id
        self.sua_base = sua_base
        self.app = app
        self.gerenciador = gerenciador

        self.g = None
        self.error_tab = False
        self.criar()

    def criar(self):
        """
        Cria a tabela

        :return: None
        """

        r = self.init()
        if not r:
            self.error_tab = True
            return self.criar()
        else:
            init_tabela, tabela = r
            if self.error_tab:
                self.app().delete_messages(chat_id=self.seu_id, message_ids=init_tabela.id - 1)
                self.error_tab = False

        self.editar_base()
        self.enviar_tabela(init_tabela, tabela)

    def init(self):
        """
        Inicia a tabela com uma mensagem de carregamento
        :return: init_tabela, tabela
        """

        self.g = self.gerenciador()
        try:
            init_tab = self.app().send_message(chat_id=self.seu_id,
                                               text=f'Iniciando tabela {self.nome_tabela}...')
            tab = json.dumps({
                'tabela': self.nome_tabela,
                'dados': [{}]
            }, indent=2)
            self.g['tabelas'][self.nome_tabela] = init_tab.id
            return init_tab, tab

        except FloodWait as e:
            print(f'FloodWait: {e.value}')
            time.sleep(e.value)
            self.init()

    def editar_base(self):
        """
        Edita a base de dados com a nova tabela
        :return: None
        """

        try:
            self.app().edit_message_text(chat_id=self.seu_id,
                                         message_id=self.sua_base,
                                         text=f'<b>TeleBase iniciado</b>\n\n'
                                              f'<code>{json.dumps(self.g, indent=2, ensure_ascii=False)}</code>\n\n'
                                              f'<i>Não apague esta mensagem!</i>')
        except FloodWait as e:
            print(f'FloodWait: {e.value}')
            time.sleep(e.value)
            self.editar_base()

    def enviar_tabela(self, init_tabela, tabela):
        """
        Envia a tabela para o usuário
        :param init_tabela: Mensagem de carregamento
        :param tabela: Tabela em formato json
        :return: None
        """

        try:
            self.app().edit_message_text(chat_id=self.seu_id,
                                         message_id=init_tabela.id,
                                         text=f'<code>{tabela}</code>')
        except FloodWait as e:
            print(f'FloodWait: {e.value}')
            time.sleep(e.value)
            self.enviar_tabela(init_tabela, tabela)
