import requests
import re
import json
import discord
from discord import app_commands
from discord.ext import commands

class AI(commands.Cog):
    """ AI chatbot """

    def __init__(self,client):
        # ollama ai is required
        # https://ollama.com

        self.url = "http://localhost"
        self.port = 11434   # standard ollama port
        self.model = "qwen" # change to your model of choice
        self.tag = "0.5b"   # change to your tag of choice

        self.client = client

    def ollama(self, generation: bool, data: dict, c_id: int):
        output = ""
        session = requests.Session()
        data.setdefault("model",f"{self.model}:{self.tag}")
        data.setdefault("stream", True)
        # greatest boilerplate to ever exist
        with session.post(f"{self.url}:{self.port}/{'/api/generate' if generation else '/api/chat'}",json=data) as out:
            for line in out.iter_lines():
                if line:
                    gen = json.loads(line)
                    if generation:
                        if gen['done'] == True: output += f"\n-# Generation time {round((gen['total_duration'])/(10**9),2)}s"
                        output += gen['response']
                    else:
                        gen = json.loads(line)
                        if gen['done'] == True:
                            self.client.messages[c_id].append({"role":"assistant","content":output})
                            output += f"\n-# Generation time {round((gen['total_duration'])/(10**9),2)}s"
                            continue
                        output += gen['message']['content']
                else:
                    pass

        return output

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or self.client.user is None: # self.client.user should not be None but pyright is getting angry at me
            return

        if not self.client.user.mentioned_in(message):
            return

        message_clean = message.content

        # message could contain mentions, so we should replace that with their usernames instead
        regex = r"<@&?(\d+)>"
        matches = re.finditer(regex,message.content)
        for match in matches:
            id = match.expand("\\1")
            user = self.client.get_user(int(id)) # int() could fail? we do check for digits..
            if not user: continue

            message_clean = message_clean.replace(match[0], user.name)

        self.client.messages.setdefault(message.channel.id, [])

        # https://github.com/ollama/ollama/blob/main/docs/api.md#chat-request-with-history
        self.client.messages[message.channel.id].append({
            "role": "user",
            "content": message_clean
        })

        output = self.ollama(False, {"messages":self.client.messages[message.channel.id]}, message.channel.id)

        await message.reply(output)

    @app_commands.command()
    async def ai(self, interaction: discord.Interaction, prompt: str):
        """ Ask AI :3
        
        Parameters
        -----------
        prompt: str
            what you should ask
        """

        if (not isinstance(interaction.channel,discord.abc.Messageable)):
            await interaction.response.send_message("Channel is not messageable ?!")
            return

        await interaction.response.send_message("Generating response, **will** take a while")

        try:
            output = self.ollama(True, {"prompt": prompt}, interaction.channel.id)
        except Exception as e:
            await interaction.edit_original_response(content=f"Exception!!!\n{e}")
            return

        await interaction.edit_original_response(content=output)

    @app_commands.command()
    async def drop_and_clean(self, interaction: discord.Interaction):
        """ Drop the message history in this channel and clean it """
        if not interaction.channel: 
            await interaction.response.send_message("bleh"); 
            return
        try:
            string = str(self.client.messages[interaction.channel.id])
        except:
            await interaction.response.send_message("ugh i die")
            return

        await interaction.response.send_message(f"```{string[:2000-6]}```") # -6 because ``` and the other ```

async def setup(bot: commands.Bot):
   await bot.add_cog(AI(bot)) 
