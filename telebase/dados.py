##"+------------------------------+"
##"! @ Author: Marcelo Batista    !"
##"! @ GitHub: /marcellobatiista  !"
##"! @ Date: 24-12-2020           !"
##"+------------------------------+"
##
##
##
##
##
##
##
import pyrogram

class Dados:

    __entidade = None
    __informacao = None
    __msg = None
    __api = None
    
    dado = None

    def __init__(self, app, entidade, informacao):

        if __name__ == '__main__':
            raise BaseException('É necessário importar a classe Dados no arquivo base.py')

        self.__api = app
        
        info = entidade
            
        if (info.type == 'channel'):
            if (info.username != None):
                raise Exception('Não é possível consultar dados em canais públicos')
        elif (entidade != 'me'):
            raise Exception('Não é possível consultar users/groups como base de dados')
        
        
        self.__entidade = info.id
                
        self.__informacao = informacao
        self.__get_msg(self.__entidade, self.__informacao)
    
        self.dado = self.__dados()
                     
            
    def __str__(self):
        if self.__msg is None:
            raise ValueError('A mensagem não foi encontrada')
        elif str(self.__msg.text)[:str(self.__msg.text).find('\n')].count('=') >= 2:
            raise Exception('Mensagem fora do padrão')
        return 'Sucesso'
    

    ''' [!] Mensagem em pyrogram.types.Message '''
    def __get_msg(self, entidade, informacao):
        #Itera mensagens com a mesma informação de busca
        for msg in enumerate(self.__api.search_messages(entidade, informacao)):
            self.__msg = msg[1]

            if msg[0] > 0:
                raise Exception('Existe duas ou mais mensagens com o mesmo identificador')
                
        
    ''' [!] Formata a mensagem recebida em string, dentro de um dicionário '''
    def __get_dict(self, msg):
        msg = str(msg)
        #Separa as linhas
        line = [p.strip() for p in msg.split('\n')]
        #Remove linhas vazias
        while '' in line:
            line.remove('')
        #Tira os espaços e transforma cada linha em uma key e value
        try:
            return dict([[x[0].strip(), x[1].strip()] for x in [p.split('=') for p in line]])
        except:
            raise Exception('A mensagem foi encontrada, mas o formato de algum dado está fora do padrão')


    ''' [!] '''
    def __editaMessage(self, new_msg):
        try:
            self.__msg = self.__api.edit_message_text(self.__entidade, self.__msg.message_id, new_msg)
            return self.__get_dict(self.__msg.text)
        except pyrogram.errors.exceptions.bad_request_400.MessageNotModified:
            # Não há modificação de mensagem
            return self.__get_dict(new_msg)  
            
    ''' [!] Dados da mensagem '''
    def __dados(self):
        self.__str__() #Aviso
        return self.__get_dict(self.__msg.text) #Dict

    ''' [!] Edita a mensagem relacionada à key e retorna um dicionário '''
    def editarValor(self, key, value):
        self.dado = self.__dados()
        new_msg = str(self.__msg.text).replace(self.dado[str(key)], str(value)) #Replace
        return self.__editaMessage(new_msg)

    ''' [!] Adiciona o dado no fim da mensagem e retorna um dicionário '''
    def adicionarDado(self, key, value):
        self.dado = self.__dados()
        if (str(key) in str(self.__msg.text)):
            raise NameError('A key já existe na mensagem')
        
        new_msg = str(self.__msg.text)+'\n'+str(key)+' = '+str(value)
        return self.__editaMessage(new_msg)

    ''' [!] Remove uma linha específica da mensagem de acordo a key recebida'''
    def removerDado(self, key):        
        new_msg = ''

        self.dado.pop(str(key))

        for frag in zip(self.dado.keys(), self.dado.values()):
            new_msg += frag[0]+' = '+frag[1]+'\n'
        new_msg = new_msg[:len(new_msg)-1]
        
        return self.__editaMessage(new_msg)
    
