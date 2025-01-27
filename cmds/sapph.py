import discord
from discord import app_commands
from discord.ext import commands

SAPPH = "<:checkmarksapph:1332467645487906876>"

class Sapphire(commands.Cog):
    """ Different commands that use a sapphire-like embed """

    def sapph_embed(self, who: discord.Member, action: str, reason: str,duration: str='Permanent'):
         """ Create an embed similar to the one made by sapphire and return it. """

         embed = discord.Embed()
         embed.add_field(name=f"{SAPPH} @{who.name} {action}", value=f"\n> **Reason**: {reason}\n> **Duration**: {duration}", inline=False)
         embed.color = discord.Colour.from_rgb(54, 206, 54)
         return embed

    def __init__(self,client: commands.Bot):
        self.client = client

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def kill(self, interaction: discord.Interaction, killee: discord.Member, reason: str='No reason provided'):
        """ Kill someone :3
        
        Parameters
        -----------
        killee: discord.Member
            person to kill
        reason: str
            reason
        """
        embed = self.sapph_embed(killee, "killed", reason)
        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def customaction(self, interaction: discord.Interaction, actionee: discord.Member, action: str, reason: str='No reason provided', duration: str='Permanent'):
        """ Whatever you want someone :3
        
        Parameters
        -----------
        actionee: discord.Member
            person to whatever you want
        action: str
            what to do in the past tense something
        reason: str
            reason
        duration: str
            duration
        """
        embed = self.sapph_embed(actionee, action, reason, duration)
        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def hug(self, interaction: discord.Interaction, hugee: discord.Member, reason: str='No reason provided'):
        """ Hug someone :3
        
        Parameters
        -----------
        hugee: discord.Member
            person to hug
        reason: str
            reason
        """
        embed = self.sapph_embed(hugee, "hugged", reason, "mrowww :3")
        embed.set_footer(text="prrrr :3")
        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def explode(self, interaction: discord.Interaction, explodee: discord.Member, reason: str='No reason provided'):
        """ Explode someone :3
        
        Parameters
        -----------
        explodee: discord.Member
            person to explode
        reason: str
            reason
        """
        embed = self.sapph_embed(explodee, "exploded", reason)
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(Sapphire(client))
