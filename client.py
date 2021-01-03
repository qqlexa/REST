from qq_rest.bot import client

bot = client.Client(name="client", ip="localhost", port=9090)
bot.print_info()
if bot.connect():
    packet = bot.recv(1024, s_type="b")
    print(packet)
