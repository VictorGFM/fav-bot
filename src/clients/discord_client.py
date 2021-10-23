import discord

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
      if message.author == self.user:
        return

      msg = message.content

      if msg.startswith('!comandos'):
          await message.channel.send('Sendo implementado... 👷‍♀️🛠️')
      if msg.startswith('!fenix'):
          await message.channel.send('Jogamos como nunca, perdemos como sempre! 🔥🐦')
      if msg.startswith('!urubus'):
          await message.channel.send('camp sexta 🦅')
      if msg.startswith('!andro'):
          await message.channel.send('Clica com direito!!!️🐧')
      if msg.startswith('!taufner'):
          await message.channel.send('Viver é sofrer ( ._.)')
      if msg.startswith('!dnie'):
          await message.channel.send('Mono Vlad Megalomaníaco 🧛🏻‍♂️')
      if msg.startswith('!exori'):
          await message.channel.send('Matabaras 🪳')
      if msg.startswith('!phelps'):
          await message.channel.send('Just smite...⚡')
      if msg.startswith('!correia'):
          await message.channel.send('Mumu 😭')
      if msg.startswith('!gilzao'):
          await message.channel.send('Mordekaiser do BIG! 🌊')
      if msg.startswith('!jalzin'):
          await message.channel.send('Papo reto 🥸')
      if msg.startswith('!nunu'):
          await message.channel.send('Nunu ta runfando porra!!! 🎃')
      if msg.startswith('!binario'):
          await message.channel.send('É o binas! 😎')
      if msg.startswith('!haayl'):
          await message.channel.send('Pisa na bolha! 🧜🏻‍♀️')
      if msg.startswith('!eastrice'):
          await message.channel.send('Odeio o taufner!')
      if msg.startswith('!xande'):
        await message.channel.send('MOROONEE!🧟‍♂️')
      if msg.startswith('!bahia'):
        await message.channel.send('~Tem uma coisa, que chama... Trabalho! Eu não sô vagabundo igual '
        +'vocês que fica jogando LoL o dia inteiro não~ sussurrando 👴🏻')
      if msg.startswith('!redfox'):
        await message.channel.send('Espera o spike do ezreal!🙅🏼‍♂️')
      if msg.startswith('!eyen'):
          await message.channel.send('Amigão...')
      if msg.startswith('!zchozen'):
          await message.channel.send('Mono Vlad 🧛🏻‍♂️')
