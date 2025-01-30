from discord.ext import commands

class TCommands(commands.Cog):
    """ Some text-based commands and funsies """

    def __init__(self, bot):
        self.client = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        self.client.index += 1

        if message.author == self.client.user:
            return

        # if "error occured" in message.content.lower():
        #    await message.channel.send("I have my suspicions that `An error occured`")


    @commands.command(name='a')
    async def _uptime(self, ctx):
        minutes = round(self.client.seconds/60,3)
        result = round((self.client.index*60)/self.client.seconds,3)

        await ctx.send(f"Total: {self.client.index} | Minutes: {minutes} | Result: {result}")

    @commands.command()
    @commands.is_owner()
    async def creload(self, ctx, cog_def: str | None):
        if cog_def:
            self.client.logger.info(f"creload ran with a cog ({cog_def}) defined.")
            await self.client.reload_extension(f"cmds.{cog_def}")
            await ctx.send("specified cog reloaded, hopefully..")
            return


        self.client.logger.info("creload ran")
        for cog in self.client.cmds_cogs:
            await self.client.reload_extension(f"cmds.{cog}")
            self.client.logger.debug(f"reloaded cmds.{cog}")

        await ctx.send("reloaded.")

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        self.client.logger.info("sync ran")
        await self.client.tree.sync()
        await ctx.send("synced.")

async def setup(bot: commands.Bot):
   await bot.add_cog(TCommands(bot)) 
