import requests
import json
import random
import discord
from discord import app_commands
from discord.ext import commands

LOADING3 = "<a:loading3:1331757666883735603>"

class Util(commands.Cog):
    """ Some weird commands that have a use but also don't. """

    def __init__(self,client: commands.Bot):
        self.client = client

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def stats(self, interaction: discord.Interaction, username: str):
        """ Gets Account statistics of a Geometry Dash account :3
        
        Parameters
        -----------
        username: str
            Username of the GD account
        """
        await interaction.response.send_message(content=f"-# {username}'s stats\n{LOADING3}`Pulling from the gdbrowser servers...`{LOADING3}")

        try:
            stats = json.loads(requests.get("http://gdbrowser.com/api/profile/" + username).text)
            output = f"`{stats['stars']} stars, {stats['diamonds']} diamonds, {stats['coins']} coins, {stats['userCoins']} user coins, {stats['demons']} demons beaten and {stats['cp']} creator points.`"
        except:
            output = "`There was an error with colon's gdbrowser servers!`"

        await interaction.edit_original_response(content=f"-# {username}'s stats\n{output}")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def uwu(self, interaction: discord.Interaction, message: str):
        """ Uwuwifies a message :3
        
        Parameters
        -----------
        message: str
            contents of the message
        """
        output = message.lower().replace("l","w").replace("r", "w").replace("the","da").replace ("i ", "i-i-i ").replace("!","!!").replace(".",".!").replace("?","?!")+" "+random.choice([":3","nyyaaa :333","rawr :3"," ~"])
        await interaction.response.send_message(output)

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def say(self, interaction: discord.Interaction, message: str):
        """ Sends a message :3
        
        Parameters
        -----------
        message: str
            contents of the message
        """
        await interaction.response.send_message(message)


async def setup(client):
    await client.add_cog(Util(client))
