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

            if message.content == Config.prefix + 'help':
                await message.channel.send('**DNW Bot Help** \n change prefix = `prefix <option>` \n show help = `help` \n ')

            if message.content == Config.prefix + 'prefix' + newPrefix:
                Config.prefix == newPrefix
                await message.channel.send('New DNW Bot prefis `' + Config.prefix + '`')

        else:
            return
        





client = MyClient()
client.run(Config.token)