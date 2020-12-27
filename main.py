from pyrogram import Client
from telebase.base import Base

app = Client(session, api_id, api_hash)

b = Base(app,'me')
me = b.consultar('357159852')

print(me.dado)

