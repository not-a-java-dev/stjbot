import random
import discord
from discord import app_commands
from discord.ext import commands

class Fun(commands.Cog):
    """ Some fun commands """

    def __init__(self,client: commands.Bot):
        self.client = client

        self.dragon_pics = open("cmds/dragons.txt").read().splitlines()

    def nick_parse(self, user: discord.User | discord.Member):
        """ Parse a discord user and if it's a member return the nickname in parenthesis if not, return an empty string"""

        nick = f"({user.nick})" if isinstance(user, discord.Member) and user.nick != None else ""

        return nick

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def furry(self, interaction: discord.Interaction):
        """ Calculates how much of a furry you are! :3 """

        nick = self.nick_parse(interaction.user)

        await interaction.response.send_message(f"-# {interaction.user.name}{nick}\nyou are {random.randint(0,100)}% a furry.")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def cool(self, interaction: discord.Interaction):
        """ Calculates how cool you are! :3 """

        nick = self.nick_parse(interaction.user)

        await interaction.response.send_message(f"-# {interaction.user.name}{nick}\nyou are {random.randint(0,100)}% cool.")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def liedetector(self, interaction: discord.Interaction):
        """ Detects if someone is lying! :3 """

        await interaction.response.send_message("-# The suspected user is lying with a chance of 100%")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ratemedia(self, interaction: discord.Interaction, link: str, containsdragons: bool):
        """ Rates a media! :3

        Parameters
        -----------
        link: str
            link of media
        containsdragons: bool
            does it contain dragons?
        """

        link = link[:2000]
        rating = "I like :3. Has dergs in it :3" if containsdragons else "Bad. No dergs. 3:"
        doesithave = "Contains dragons :3" if containsdragons else "Doesn't contain dragons."

        await interaction.response.send_message(f"-# Rating of media {link}\n-# {doesithave}\nRating: `{rating}`")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def dragon(self, interaction: discord.Interaction):
        """ Sends a pretty dragon picture :3 """

        nick = self.nick_parse(interaction.user)

        await interaction.response.send_message(f"-# {interaction.user.name}{nick}\n-# Random dragon:\n{random.choice(self.dragon_pics)}")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def fooycord(self, interaction: discord.Interaction, user: discord.Member):
        """ Checks if someone uses fooycord :3

        Parameters
        -----------
        user: discord.Member
            the user in question
        """

        result = "Status: Not a fooycord user"
        banned = False
        # previous result
        p_result = result

        # uses = "USER DOES NOT USE FOOYCORD"
        if user.id == 1015031565950140457:
            result = "Status: Fooycord owner"
        elif user.id == 1045761412489809975:
            result = "Status: Fooycord official partner"
        elif user.id == 978053871270248508:
            result = "Status: Fooycord + user"
        elif user.id == 998995432132853891:
            banned = True
            result = "Status: Banned from fooycord for making spyware"
            uses = "USER IS BANNED FROM FOOYCORD"
        elif user.id == 940959889126219856:
            banned = True
            result = "Status: Banned from fooycord for violating fooycord tos"
            uses = "USER IS BANNED FROM FOOYCORD"

        uses = "USER IS IN FOOYCORD DATABASE " if result != p_result and not banned else "USER DOES NOT USE FOOYCORD"

        await interaction.response.send_message(f"-# OFFICIAL fooycord checker\n-# Result for <@{user.id}>:\n{uses}\n{result}")

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def bubblewrap(self, interaction: discord.Interaction):
        """ Pop the bubbles :3 """

        # uhh.. at least it's better than tjc's bot source code right? .. right???
        bubble = "\n" + ( ( "||  o  ||" * 8 ) + "\n" ) * 8

        await interaction.response.send_message(f"Bubble wrap! {bubble}");

async def setup(client):
    await client.add_cog(Fun(client))
