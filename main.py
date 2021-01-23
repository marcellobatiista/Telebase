from pyrogram import Client
from telebase.dados import Dados

app = Client(session, api_id, api_hash)

class Bot:
  
  base = None
  
  def __init__(self, client):
    self.base = Dados(client, 'https://')
    
  def example(self):
    self.base.buscar(bot.from_user.id)
    
    data = self.base.dados()
    set_data = self.base.editarValor("contato", "+55 71 9 0000-0000")
    add_data = self.base.adicionarDado("email", "@")
    remove_data = self.base.removerDado("email")
    
    bag = [data, set_data, add_data, remove_data]
    
    for b in bag:
      print(b)
