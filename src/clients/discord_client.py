import discord

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
      if message.author == self.user:
        return

      msg = message.content

      if msg.startswith('!comandos'):
          await message.channel.send('Sendo implementado... ð·ââï¸ð ï¸')
      if msg.startswith('!fenix'):
          await message.channel.send('Jogamos como nunca, perdemos como sempre! ð¥ð¦')
      if msg.startswith('!urubus'):
          await message.channel.send('camp sexta ð¦')
      if msg.startswith('!andro'):
          await message.channel.send('Clica com direito!!!ï¸ð§')
      if msg.startswith('!taufner'):
          await message.channel.send('Viver Ã© sofrer ( ._.)')
      if msg.startswith('!dnie'):
          await message.channel.send('Mono Vlad MegalomanÃ­aco ð§ð»ââï¸')
      if msg.startswith('!exori'):
          await message.channel.send('Matabaras ðª³')
      if msg.startswith('!phelps'):
          await message.channel.send('Just smite...â¡')
      if msg.startswith('!correia'):
          await message.channel.send('Mumu ð­')
      if msg.startswith('!gilzao'):
          await message.channel.send('Mordekaiser do BIG! ð')
      if msg.startswith('!jalzin'):
          await message.channel.send('Papo reto ð¥¸')
      if msg.startswith('!nunu'):
          await message.channel.send('Nunu ta runfando porra!!! ð')
      if msg.startswith('!binario'):
          await message.channel.send('Ã o binas! ð')
      if msg.startswith('!haayl'):
          await message.channel.send('Pisa na bolha! ð§ð»ââï¸')
      if msg.startswith('!eastrice'):
          await message.channel.send('Odeio o taufner!')
      if msg.startswith('!xande'):
        await message.channel.send('MOROONEE!ð§ââï¸')
      if msg.startswith('!bahia'):
        await message.channel.send('~Tem uma coisa, que chama... Trabalho! Eu nÃ£o sÃ´ vagabundo igual '
        +'vocÃªs que fica jogando LoL o dia inteiro nÃ£o~ sussurrando ð´ð»')
      if msg.startswith('!redfox'):
        await message.channel.send('Espera o spike do ezreal!ðð¼ââï¸')
      if msg.startswith('!eyen'):
          await message.channel.send('AmigÃ£o...')
      if msg.startswith('!zchozen'):
          await message.channel.send('Mono Vlad ð§ð»ââï¸')
