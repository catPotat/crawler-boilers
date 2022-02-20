from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord.utils import get


class DiscordClient(discord.Client):
    async def on_ready(self):
        try:
            print(f'We have logged in as {self.user}')
            '''
            cur_chan = self.get_channel(int(input("Channel ID: ")))
            await cur_chan.send(input("Message to send: "))
            '''
            
            
            member = self.get_user(510768840972566528)
            print(member)
            guild = self.get_guild(489461408174571521)
            print(guild)
            role = get(guild.roles, name="Lucifer")
            print(role)
            await member.add_roles(role)

        except Exception as e:
            print()
            print(e)
        await self.close()


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.members = True
    my_client = DiscordClient(intents=intents)
    
    TOKEN = os.getenv('REEBOT_TOKEN')
    my_client.run(TOKEN, bot=True)