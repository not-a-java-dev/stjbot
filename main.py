import logging
import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks

class TJBot(Bot):

    def __init__(self,intents: discord.Intents):

        # random string so that the bot doesnt acknowledge normal messages
        super().__init__(command_prefix='st!', intents=intents, activity=discord.CustomActivity(name='stupid horse'), help_command=None)

        self.logger = logging.getLogger('discord')

        # amount of messages that went through on_message
        self.index = 0
        # seconds since the setup hook starts
        self.seconds = 0

        self.cmds_cogs = ["tcommands","util", "sapph", "fun", "quote"]

    async def setup_hook(self):
        self.m_activity.start()

    async def on_ready(self):
        client.logger.info("Ready.")

        for cog in client.cmds_cogs:
            client.logger.debug(f"cmds.{cog} loaded")
            await client.load_extension(f"cmds.{cog}")

    @tasks.loop(seconds=1)
    async def m_activity(self):
        self.seconds += 1


if __name__ == "__main__":
    TOKEN = os.environ.get('TOKEN')

    if not TOKEN:
        print("no TOKEN environment variable found!\nPlease set one <3")
        exit(1)

    intents = discord.Intents.all()
    client = TJBot(intents=intents)


    handler = logging.FileHandler(filename='tjbot.log', encoding='utf-8', mode='w')

    logging.getLogger('discord.http').setLevel(logging.INFO)
    logging.getLogger('discord.client').setLevel(logging.INFO)
    logging.getLogger('discord.gateway').setLevel(logging.INFO)

    intro = open("intro")
    print(intro.read())
    intro.close()

    client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)

