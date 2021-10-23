from decouple import config

from server import server
from clients.discord_client import *

disc_client = DiscordClient()
server.keep_alive()
disc_client.run(config("TOKEN"))