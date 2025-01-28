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
        if message.content == "st!a":
            minutes = round(self.client.seconds/60,3)
            result = round((self.client.index*60)/self.client.seconds,3)

            await message.channel.send(f"Total: {self.client.index} | Minutes: {minutes} | Result: {result}")
            return

        is_owner = await self.client.is_owner(message.author)
        # sync the commands
        if message.content == "st!sync" and is_owner:
            self.client.logger.info("sync ran")
            await self.client.tree.sync()
            await message.channel.send("synced.")
            return

        # reload cogs
        if message.content == "st!creload" and is_owner:
            self.client.logger.info("creload ran")
            for cog in self.client.cmds_cogs:
                await self.client.reload_extension(f"cmds.{cog}")
                self.client.logger.debug(f"reloaded cmds.{cog}")

            await message.channel.send("reloaded.")
            return

        # if "error occured" in message.content.lower():
        #    await message.channel.send("I have my suspicions that `An error occured`")


async def setup(bot: commands.Bot):
   await bot.add_cog(TCommands(bot)) 
