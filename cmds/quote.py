import base64
import random
import discord
from discord import app_commands
from discord.ext import commands

LOADING3 = "<a:loading3:1332467109371973797>"

class Quotes(commands.Cog):
    """ Quote winter's messages (hard-coded) """

    def __init__(self,client: commands.Bot):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id != 978053871270248508:
            return

        nick = ""
        if isinstance(message.author, discord.Member) and message.author.nick != None:
            nick = base64.b64encode(message.author.nick.encode()).decode()

        message_content = base64.b64encode(message.content.encode())
        message_parsed = f"{message.author.name}~{nick}~{message_content.decode()}"

        print(f"logged winter's message as {message_parsed}")
        with open("w_mesg.txt", "a") as w_mesg:
            w_mesg.write(f"{message_parsed}\n")
            pass

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def quote(self, interaction: discord.Interaction):
        """ Sends a random quote :3 """

        nick = f"({interaction.user.nick})" if isinstance(interaction.user, discord.Member) and interaction.user.nick != None else ""
        await interaction.response.send_message(f"-# {interaction.user.name}{nick}\n-# Random quote:\n{LOADING3}`Please wait... Searching logs...`")

        with open("w_mesg.txt", "r") as logs:
            message = random.choice(logs.read().splitlines())

            username, nickname_b64, message_b64 = message.split("~")

            nickname_decoded = base64.b64decode(nickname_b64.encode()).decode()
            message_decoded = base64.b64decode(message_b64.encode()).decode()

            if nickname_decoded != "":
                nickname_decoded = f"({nickname_decoded})"

            parsed_quote = f"-# Quote from {username}{nickname_decoded}\n{message_decoded}"

            await interaction.edit_original_response(content=parsed_quote)

async def setup(client):
    await client.add_cog(Quotes(client))
