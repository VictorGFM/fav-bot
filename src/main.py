from decouple import config

from clients.discord_client import *

disc_client = DiscordClient()
disc_client.run(config("TOKEN"))