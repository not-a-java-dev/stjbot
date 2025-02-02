import base64
import time
import random
import discord
from discord import app_commands
from discord.ext import commands

LOADING3 = "<a:loading3:1332467109371973797>"

class Quotes(commands.Cog):
    """ Quote tjc's messages (hard-coded) """

    def __init__(self,client: commands.Bot):
        self.client = client
        self.qf_ctx_menu = app_commands.ContextMenu(
            name="Force quote",
            callback=self.quote_force
        )

        self.client.tree.add_command(self.qf_ctx_menu)

    async def cog_unload(self):
        self.client.tree.remove_command(self.qf_ctx_menu.name, type=self.qf_ctx_menu.type)


    def mesg_quote(self, message: discord.Message):

        nick = ""
        if isinstance(message.author, discord.Member) and message.author.nick != None:
            nick = base64.b64encode(message.author.nick.encode()).decode()
        else:
            nick = base64.b64encode(message.author.display_name.encode()).decode()

        if message.author.display_name == message.author.name:
            nick = ""

        message_content = base64.b64encode(message.content.encode())
        message_parsed = f"{message.author.name}~{nick}~{message_content.decode()}"

        with open("t_mesg.txt", "a") as w_mesg:
            w_mesg.write(f"{message_parsed}\n")


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id != 1045761412489809975:
            return

        self.mesg_quote(message)

    @app_commands.command()
    async def quote(self, interaction: discord.Interaction):
        """ Sends a random quote :3 """

        nick = f"({interaction.user.nick})" if isinstance(interaction.user, discord.Member) and interaction.user.nick != None else ""
        await interaction.response.send_message(f"-# {interaction.user.name}{nick}\n-# Random quote:\n{LOADING3} `Please wait... Searching logs...`")
        time.sleep(0.2) # :troll:

        with open("t_mesg.txt", "r") as logs:
            try:
                message = random.choice(logs.read().splitlines())
            except:
                await interaction.edit_original_response(content="Error! No logged messages maybe?")
                return

            username, nickname_b64, message_b64 = message.split("~")

            nickname_decoded = base64.b64decode(nickname_b64.encode()).decode()
            message_decoded = base64.b64decode(message_b64.encode()).decode()

            if nickname_decoded != "":
                nickname_decoded = f"({nickname_decoded})"

            parsed_quote = f"-# Quote from {username}{nickname_decoded}\n{message_decoded}"

            await interaction.edit_original_response(content=parsed_quote)

    async def quote_force(self, interaction: discord.Interaction, message: discord.Message):
        """ Quote tjc forcefully """

        print(f"grahh {message.author}")
        is_owner = await self.client.is_owner(interaction.user)
        if not is_owner:
            await interaction.response.send_message(f"nah {interaction.user.name}",ephemeral=True)
            return

        await interaction.response.send_message(message.content,ephemeral=True)
        self.mesg_quote(message)

async def setup(client):
    await client.add_cog(Quotes(client))
