from pyrogram import Client
from telebase.dados import Dados

app = Client(session, api_id, api_hash)

class Bot:
  
  base = None
  
  def __init__(self, client):
    self.base = Dados(client, 'https://')
    
  def search(self, info):
    self.base.buscar(info)
    
  def get_data(self):
    return self.base.dados()
  
  def set_value(self, key, new_value):
    return self.base.editarValor(key, new_value)
  
  def add_line(self, key, value):
    return self.base.adicionarDado(key, value)
  
  def remove_data(self, key):
    return self.base.removerDado(key)
