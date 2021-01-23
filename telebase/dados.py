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
import pyrogram, time

class Dados:

    entidade = None
    __msg = None
    __api = None

    def __init__(self, app, entidade):
        
        if __name__ == '__main__':
            raise BaseException('É necessário importar a classe Dados')
        
        app.start()
        
        print('<----| Client iniciado |---->\n')
        print('Carregando base de dados...')
        
        info = app.get_chat(entidade)
        self.__api = app
            
        if (info.type == 'channel'):
            if (info.username != None):
                raise Exception('Não é possível consultar dados em canais públicos')
        elif (entidade != 'me'):
            raise Exception('Não é possível consultar users/groups como base de dados')
        
        self.entidade = info.id
        
            
    def __str__(self):
        if self.__msg is None:
            raise ValueError('A mensagem não foi encontrada')
        elif str(self.__msg.text)[:str(self.__msg.text).find('\n')].count('=') >= 2:
            raise Exception('Mensagem fora do padrão')
        return 'Sucesso'
    

    def buscar(self, informacao):
        ''' [!] Mensagem em pyrogram.types.Message '''
        #Itera mensagens com a mesma informação de busca
        for msg in self.__api.search_global(query=informacao, limit = 1):
            self.__msg = msg
        
    def __get_dict(self, msg):
        ''' [!] Formata a mensagem recebida em string, dentro de um dicionário '''
        try:
            return {p.strip().split('=')[0].strip() : p.strip().split('=')[1].strip() 
                    for p in str(msg).split('\n') if p != ''}
        except:
            raise Exception('A mensagem foi encontrada, mas o formato de algum dado está fora do padrão')


    def __editaMessage(self, new_msg):
        ''' [!] '''
        try:
            self.__msg = self.__api.edit_message_text(self.__msg.chat.id, self.__msg.message_id, new_msg)
            return self.__get_dict(self.__msg.text)
        except pyrogram.errors.exceptions.bad_request_400.MessageNotModified:
            # Não há modificação de mensagem
            return self.__get_dict(new_msg)
    
    def __dict_to_text(self, dado):
        ''' [!] Dict to text '''
        new_msg = ''
        
        for key, value in dado.items():
            new_msg += key+' = '+value+'\n'
        new_msg = new_msg[:len(new_msg)-1]
        
        return new_msg
            
    def dados(self):
        ''' [!] Dados da mensagem '''
        try:
            self.__str__() #Aviso
            return self.__get_dict(self.__msg.text) #Dict
        except:
            pass #print('A mensagem retornou vazia ou fora do padrão')
            
    def editarValor(self, key, value):
        ''' [!] Edita a mensagem relacionada à key e retorna um dicionário '''
        dado = self.dados()
        dado[key] = value
        new_msg = self.__dict_to_text(dado)
        
        return self.__editaMessage(new_msg)

    def adicionarDado(self, key, value):
        ''' [!] Adiciona o dado no fim da mensagem e retorna um dicionário '''
        if (str(key) in str(self.__msg.text)):
            raise NameError('A key já existe na mensagem')
        
        new_msg = str(self.__msg.text)+'\n'+str(key)+' = '+str(value)
        return self.__editaMessage(new_msg)

    def removerDado(self, key):
        ''' [!] Remove uma linha específica da mensagem de acordo a key recebida'''   
        dado = self.dados().pop(str(key))
        new_msg = self.__dict_to_text(dado)
        
        return self.__editaMessage(new_msg)
    
