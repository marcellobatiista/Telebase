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

    __msg = None
    __api = None

    def __init__(self, app):
        
        if __name__ == '__main__':
            raise BaseException('É necessário importar a classe Dados')
        
        app.start()
        print('<----| Client iniciado |---->\n')
        self.__api = app
            
    def __str__(self):
        if self.__msg is None:
            raise ValueError('A mensagem não foi encontrada')
        elif str(self.__msg.text)[:str(self.__msg.text).find('\n')].count('=') >= 2:
            raise SyntaxError('Linha com 2+ igualdades')
        return 'Sucesso'
    

    def buscar(self, id, ref):
        ''' [!] Mensagem em pyrogram.types.Message '''
        #Itera mensagens com a mesma informação de busca
        informacao = str(ref) + ' ' + str(id)
        
        found = None
        for msg in self.__api.search_global(query=informacao, limit = 1):
            self.__msg = msg
            found = True
        
        if not (found):
            self.__msg = found
        
    def __get_dict(self, msg):
        ''' [!] Formata a mensagem recebida em string, dentro de um dicionário '''
        try:
            return {p.strip().split('=')[0].strip() : p.strip().split('=')[1].strip() 
                    for p in str(msg).split('\n') if p != ''}
        except IndexError:
            raise IndexError('Mensagem com erro de sintaxe')


    def __editaMessage(self, new_msg):
        ''' [!] '''
        tipo = type(new_msg) == dict 
        
        if (tipo):
            new = self.__dict_to_text(new_msg)
        else:
            new = new_msg
            
        try:
            self.__msg = self.__api.edit_message_text(self.__msg.chat.id, self.__msg.message_id, new)
        except pyrogram.errors.exceptions.bad_request_400.MessageNotModified:
            pass
        
        if (tipo):
            return new_msg
        else:
            return self.__get_dict(self.__msg.text)
    
    def __dict_to_text(self, dado):
        ''' [!] '''
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
        except ValueError: #Msg não encontrada
            return None
            
    def editarValor(self, key, value):
        ''' [!] Edita a mensagem relacionada à key e retorna um dicionário '''
        dado = self.dados()
        dado[key] = value
        
        return self.__editaMessage(dado)

    def adicionarDado(self, key, value):
        ''' [!] Adiciona o dado no fim da mensagem e retorna um dicionário '''
        if (str(key) in str(self.__msg.text)):
            raise NameError('A key já existe na mensagem')
        
        new_msg = str(self.__msg.text)+'\n'+str(key)+' = '+str(value)
        return self.__editaMessage(new_msg)

    def removerDado(self, key):
        ''' [!] Remove uma linha específica da mensagem de acordo a key recebida'''   
        dado = self.dados().pop(str(key))
        
        return self.__editaMessage(dado)
