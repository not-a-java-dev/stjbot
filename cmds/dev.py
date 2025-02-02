import discord
import base64
from typing import List
from discord import app_commands
from discord.ext import commands

class Dev(commands.Cog):
    """ Some fun commands """

    def __init__(self,client: commands.Bot):
        self.client = client

    @app_commands.command()
    async def eval(self, interaction: discord.Interaction, prompt: str):
        """ Evaluate some code (OWNER ONLY) """

        is_owner = await self.client.is_owner(interaction.user)

        if not is_owner:
            await interaction.response.send_message("if you said nicely maybe")
            return

        if "TOKEN" in prompt:
            await interaction.response.send_message("uh sure brb")
            return

        # spooky!
        try:
            result = eval(prompt)
        except:
            await interaction.response.send_message("https://www.w3schools.com/python/default.asp")
            return

        await interaction.response.send_message(f"```{result}```")

    @app_commands.command()
    async def dev(self, interaction: discord.Interaction, prompt: str):
        """ Some developer stuff

        Parameters
        -----------
        prompt: str
            prompt
        """

        if await self.client.is_owner(interaction.user):
            await interaction.response.send_message("bonk")
            return

        if prompt == "dump":
            with open("t_mesg.txt", "rb") as log:
                await interaction.response.send_message(file=discord.File(log))
            return

        if prompt == "cogs": await interaction.response.send_message(', '.join(self.client.cogs))
        
        try:
            command, value = prompt.split("=", 1)
        except:
            await interaction.response.send_message("bonk bonk")
            return

        if command == "search":
            output = ""
            output1 = "-# Message Finder\n"
            hits = 0

            with open("t_mesg.txt") as log:
                for line in log.read().splitlines():
                    username, nickname_b64, message_b64 = line.split("~")
                    nickname = base64.b64decode(nickname_b64.encode()).decode()
                    message = base64.b64decode(message_b64.encode()).decode()

                    if value not in message:
                        continue
                    if hits > 10:
                        break

                    hits += 1
                    output += f"```{username} ({nickname}): {message}```"

                output1 += f"{hits} {'hit' if hits == 1 else 'hits'}"
                output = "Nothing found :(" if output == "" else output

            await interaction.response.send_message(f"{output1}\n{output}")

            return

    @dev.autocomplete(name='prompt')
    async def dev_ac(self, _: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        def_prompts = ['search=', 'dump', 'cogs']
        if current in def_prompts: return []

        return [
            app_commands.Choice(name=default_prompt, value=default_prompt)
            for default_prompt in def_prompts if current.lower() in default_prompt.lower()
        ]

async def setup(client):
    await client.add_cog(Dev(client))
