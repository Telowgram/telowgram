from telethon import TelegramClient

api_id = api id here
api_hash = 'api hash here'

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))
