from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from pyro import validate_session

APP_ID = os.environ.get("22758461")
APP_HASH = os.environ.get("6cffe5b771ca80bdfe8a711f333d8222")

ss = os.environ.get("1BVtsOKABuxRJxUauNNheV805_yShEL02H4TDgnUYtm_xG6xehctH0a5fVrsept045sss-Zo6RLmf0My2Aiv2mWTe0-YUbP7291tdHI3k3WHPRdxZxHJBGo5UPqXdgQIrotakXqfhGPfbY6JP7Uvb3WwhiOkQ6EyiwgQmE1g5g2nZs6-qOXAftQR9wTJxhtXcnW29sSftpXyTEa-9FVKoTKhsi8OCNzucNfGUBVS40Urg2oLpIhyqeJu46DvIindHf6h-toYNu8MHAQNVX57uX9Md9fFPCHPZFhUuSxdk7AJQHjxYHae3qs7uMs8-INZ2f88v6WEHVhJh13y4lTpwPTkq5g5TIoA=")
session = validate_session(ss)
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# BOT_USERNAME = os.environ.get("BOT_USERNAME")
# token = os.environ.get("TOKEN")
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()