from dotenv import load_dotenv
load_dotenv()
import os

os.system('cls')

## MongoDB client
MONG_USER = os.getenv('MONG_USER')
MONG_PWD  = os.getenv('MONG_PWD')
MONG_HOST = os.getenv('MONG_HOST')
MONG_PORT = os.getenv('MONG_PORT')
DATABASE = "dataDumpingGround"

from pymongo import MongoClient
from bson.objectid import ObjectId

uri = f"mongodb://{MONG_USER}:{MONG_PWD}@{MONG_HOST}:{MONG_PORT}/{DATABASE}"
client = MongoClient(uri)
db = client[DATABASE]
print(db)


## Discord.py client
from sys import maxsize as inf
OFFSET = 0
LIMIT = 20000 # performance reason
USER_SNOWFLAKE = 120736323706421249

import discord
from pprint import pprint
from datetime import datetime, timezone, timedelta
from helperfunctions import (
    substr_matches,
    compress_object,
)

class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

        ## Get user info
        user = self.user
        print(user)

        # https://discordpy.readthedocs.io/en/latest/api.html?highlight=message#id7
        attrs_to_save = [
            'avatar', 'avatar_url', 'bot', 'colour', 'created_at',
            'default_avatar','default_avatar_url', 'discriminator',
            'display_name', 'id', 'name', 'public_flags', 'system',
        ]

        my_user_dict = {attr : getattr(user, attr) for attr in user.__dir__()}
        user_obj = compress_object(my_user_dict, attrs_to_save)
        user_obj['Last updated'] = datetime.now(tz=timezone(timedelta(hours=+7)))
        pprint(user_obj)

        ### Save to db
        profile_col = db["discordProfiles"]
        key = {'id': user_obj['id']}
        profile_col.update(key, user_obj, upsert=True)
        exit()


        ## Get messages from channels
        import re
        from tqdm import tqdm
        
        for guild in self.guilds:
            if substr_matches(guild.name, ['eevee', 'hub']):
                break
        
        for channel in guild.channels:
            if not substr_matches(channel.name, ['general', 'eevee'], exact=1):
                continue
            if not hasattr(channel, 'history'):
                continue
            print(channel.name)
            async for msg in channel.history(limit=LIMIT) :
                OFFSET -= 1
                if OFFSET>0:
                    continue
                
                
                attr_ls = msg.__dir__()
                print(attr_ls)
                filtered = [ele for ele in attr_ls if not ele.startswith('_')]
                pprint(filtered)

                # playground
                print(msg.created_at)
                print(str(msg.created_at)[11:13])
                print(msg.created_at.hour)

                for attr in filtered:
                    print(attr)
                    print(getattr(msg, attr))
                exit()


## ok
TOKEN = os.getenv('MY_DISCORD_TOKEN')
if __name__ == "__main__":
    my_client = DiscordClient()
    my_client.run(TOKEN, bot=False)