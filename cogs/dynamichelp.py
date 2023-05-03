import nextcord
from nextcord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = nextcord.Embed(title='Help', description='List of available commands:', color=nextcord.Color.blue())

        for cog, commands in mapping.items():
            if cog:
                cog_name = cog.qualified_name
                cog_commands = [f"{command.name}: {command.description}" for command in commands if not command.hidden]
                if cog_commands:
                    embed.add_field(name=cog_name, value='\n'.join(cog_commands), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = CustomHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

def setup(bot):
    bot.add_cog(HelpCog(bot))
