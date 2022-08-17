from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters

api_id =
api_hash = ""

app = Client('bot', api_id, api_hash)
print('R U N')


@app.on_message(filters.private)
def swnd_code(Client, m: Message):
    if m.chat.id == 777000:
        print(m.text)


app.run()
