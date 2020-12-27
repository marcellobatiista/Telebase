##"+------------------------------+"
##"! @ Author: Marcelo Batista    !"
##"! @ GitHub: /marcellobatiista  !"
##"! @ Date: 25-12-2020           !"
##"+------------------------------+"
##
##
##
##
##
##
##


from telebase.dados import Dados


class Base(Dados):

    __api = None
    __entidade = None
    
    def __init__(self, app, entidade = None):
        if __name__ == '__main__':
            raise BaseException('É necessário importa a classe Base em outro arquivo .py')

        self.__api = app
        self.__entidade = entidade
        
        
    def consultar(self, informacao, entidade = None):
        if entidade == None:
            return Dados(self.__api, self.__entidade, informacao)
        elif entidade != None and self.__entidade == None:
            return Dados(self.__api, entidade, informacao)
        else:
            raise Exception('O username/ID já foi argumentado no construtor da classe Base')


