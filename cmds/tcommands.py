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

        # no real use, stays here because cool
        if message.content == "!a":
            await message.channel.send(f"Total: {self.client.index} | Minutes: {round(self.client.seconds/60,3)} | Result: {round((self.client.index*60)/self.client.seconds,3)}")
        is_owner = await self.client.is_owner(message.author)
        # sync the commands
        if message.content == "!tsync" and is_owner: 
            self.client.logger.info("!tsync ran")
            await self.client.tree.sync()
            await message.channel.send("synced.")

        # reload cogs
        if message.content == "!creload" and is_owner: 
            self.client.logger.info("!creload ran")
            for cog in self.client.cmds_cogs:
                await self.client.reload_extension(f"cmds.{cog}")
                self.client.logger.debug(f"reloaded cmds.{cog}")

            await message.channel.send("reloaded.")

        if "error occured" in message.content.lower():
            await message.channel.send("`An error occured`")


async def setup(bot: commands.Bot):
   await bot.add_cog(TCommands(bot)) 
