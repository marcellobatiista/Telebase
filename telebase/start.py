from typing import Union
from telebase.bot import Bot
from telebase.tabela import Tabela
from telebase.gerenciador import Gerenciador
from telebase.criar_tabela import CriarTabela


class TeleBase(Gerenciador):

    version = None

    def __init__(self, seu_id: int = None, sua_base: int = None):
        """
        :param seu_id: ID do chat que irá gerenciar o banco de dados
        :param sua_base: ID da sua base de dados gerada
        """

        super().__init__(seu_id, sua_base)  # Inicia o gerenciador
        self.seu_id = seu_id
        self.sua_base = sua_base
        self.tokens = None

    def __params(self):
        """
        Cria um objeto Tabela com os parâmetros necessários

        :return: Tabela com seus respectivos métodos
        """

        tabela = Tabela(self.seu_id,
                        self.sua_base,
                        self.gerenciador,
                        self.app)
        return tabela

    def criar_database(self):
        return self.__params().criar_database(self)

    def drop_database(self):
        return self.__params().drop_database()

    def adicionar_bot(self, tokens: Union[list, str]):
        self.tokens = tokens
        if isinstance(tokens, str):
            tokens = [tokens]
        for token in tokens:
            self.bots.append(Bot(token).cliente)

    def iniciar_bot(self):
        for bot in self.bots:
            bot.start()
            bot.name = bot.get_me().username
            print(f'Bot @{bot.name} iniciado com sucesso!')

    def criar_tabela(self, nome_tabela: str):
        CriarTabela(nome_tabela,
                    self.seu_id,
                    self.sua_base,
                    self.gerenciador,
                    self.app)

    def get_tabela(self, nome_tabela: str):
        return self.__params().get_tabela(nome_tabela)

    def drop_tabela(self, nome_tabela: str):
        return self.__params().drop_tabela(nome_tabela)

    def add(self, nome_tabela, chave: str, valor):
        return self.__params().add(nome_tabela, chave, valor)

    def get(self, nome_tabela, chave: str):
        return self.__params().get(nome_tabela, chave)

    def delete(self, nome_tabela, chave: str):
        return self.__params().delete(nome_tabela, chave)

    def update(self, nome_tabela, chave: str, valor):
        return self.__params().update(nome_tabela, chave, valor)

    def get_all(self, nome_tabela: str):
        return self.__params().get_all(nome_tabela)

    def get_all_keys(self, nome_tabela: str):
        return self.__params().get_all_keys(nome_tabela)

    def get_all_values(self, nome_tabela: str):
        return self.__params().get_all_values(nome_tabela)
