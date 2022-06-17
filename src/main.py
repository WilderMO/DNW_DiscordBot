import discord
import Config

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)



    async def on_message(self, message):
        # don't respond to ourselves
        
        if message.content[0] == Config.prefix:
            
            if message.author == self.user:
                return

            if message.content == Config.prefix + 'ping':
                await message.channel.send('pong')


        else:
            return
        





client = MyClient()
client.run(Config.token)