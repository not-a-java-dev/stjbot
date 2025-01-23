import random
import discord
from discord import app_commands
from discord.ext import commands

class Fun(commands.Cog):
    """ Some fun commands """

    def __init__(self,client: commands.Bot):
        self.client = client
        self.dragon_pics = ["https://cdn.discordapp.com/attachments/1268366668384440352/1296478069644857456/daily-wof-n-6-is-for-moonwatcher-because-book-6-lol-v0-posa9i0vrqrd1.png?ex=67126ecb&is=67111d4b&hm=8120b56b35ad3efb51a3f386810bdd86474aad24ad7fbee46f2c6d4a3c710303&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454647988785203/Screenshot_2024-09-28_010620.png?ex=67120168&is=6710afe8&hm=ec5b8c4d1c634e6eb9a53351ef8ca4fe6bceb05744e9280fc0875a8f8e06d146&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454648270061680/Screenshot_2024-09-28_010632.png?ex=67120168&is=6710afe8&hm=74f790133c4c1cb2d1b4acaa4afeada331bd325adb4f0f1d4311b353f166eed6&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454648546623580/Screenshot_2024-09-28_010636.png?ex=67120168&is=6710afe8&hm=3da7381c75fc64e0a61578fab0319d4f44a34757a245eaeb918971010a98099f&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454648810995784/Screenshot_2024-09-28_010642.png?ex=67120168&is=6710afe8&hm=03cfbc24966ea8432ce7c97af5441b3822bb0eb1938822689508afdd6a05cb9a&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454649293213707/Screenshot_2024-09-26_224025.png?ex=67120168&is=6710afe8&hm=dea568bc9f61cf8b0c0bf97a174632ca179b306775959d47d41f4960553ed048&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295829796785356921/356820797_820021332821117_4782542855209346236_n.png?ex=67120d4a&is=6710bbca&hm=ea44dcf5b71c89e4e7d187353b2c403508bcbc0faed0ca6ef00ed627ec8cbced&", "https://cdn.discordapp.com/attachments/755132919202316409/1296847095210184725/Dragon_kisser.jpg?ex=671a5df9&is=67190c79&hm=a924044678cac0f620abb5f834285f5e03d098b1a460e0e9f020da4b2f1534e1&"]

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def furry(self, interaction: discord.Interaction):
        """ Calculates how much of a furry you are! :3 """

        nick = "None"
        if isinstance(interaction.user,discord.Member):
            nick = interaction.user.nick
        
        await interaction.response.send_message(f"-# {interaction.user.name}({nick})\nyou are {random.randint(0,100)}% a furry.")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def cool(self, interaction: discord.Interaction):
        """ Calculates how cool you are! :3 """

        nick = "None"
        if isinstance(interaction.user,discord.Member):
            nick = interaction.user.nick
        await interaction.response.send_message(f"-# {interaction.user.name}({nick})\nyou are {random.randint(0,100)}% cool.")


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

        rating = "I like :3. Has dergs in it :3" if containsdragons else "Bad. No dergs. 3:"
        doesithave = "Contains dragons :3" if containsdragons else "Doesn't contain dragons."

        await interaction.response.send_message(f"-# Rating of media {link}\n-# {doesithave}\nRating: `{rating}`")


    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def dragon(self, interaction: discord.Interaction):
        """ Sends a pretty dragon picture :3 """

        nick = "None" # Make similar behaviour to TJBot
        if isinstance(interaction.user,discord.Member):
            nick = interaction.user.nick
        await interaction.response.send_message(f"-# {interaction.user.name}({nick})\n-# Random dragon:\n{random.choice(self.dragon_pics)}")


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

async def setup(client):
    await client.add_cog(Fun(client))
