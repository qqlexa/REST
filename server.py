from qq_rest.bot.server import *
import asyncio

bot = Server(name="client", ip="localhost", port=9090)

bot.create_server()
bot.accept()
bot.send("Hello", "t")
bot.print_info()
