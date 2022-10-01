import os
import discord
from discord import Intents
from discord.ext import commands
import asyncio

emoji_lol = '<:pngwing:1025537792165560400>'
emoji_lor = '<:Legends_Of_Runeterra_Monogram:1025537107244089436>'
emoji_valorant = '<:valorant:1025537117436268584>'
emoji_apex = '<:dczo00vfc29c0d04cdd4ee9b95d64258:1025537088453619712>'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot foi conectado {0}! OLÁ MUNDO!!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.upper() == 'OLA' or message.content.upper() == 'OLÁ':
            created_message = await message.channel.send(f'Bem vindo, ao mais novo gamer {message.author.name} !! espero que se sinta a vontade.\nEscolha seu jogo favorito reagindo aos emotes abaixo para desbloquear sua comunidade! \n')
            await created_message.add_reaction(emoji_lol)
            await created_message.add_reaction(emoji_valorant)
            await created_message.add_reaction(emoji_lor)
            await created_message.add_reaction(emoji_apex)


    async def on_reaction_add(self,reaction, user):
        msg = reaction.message

        if str(reaction.emoji) == emoji_lor:
            role = discord.utils.find(lambda r: r.name == "LoR", msg.guild.roles)
            await user.add_roles(role)
            print("Cargo adicionado com sucesso!")

        if str(reaction.emoji) == emoji_valorant:
            role = discord.utils.find(lambda r: r.name == "Valorant", msg.guild.roles)
            await user.add_roles(role)
            print("Cargo adicionado com sucesso!")

        if str(reaction.emoji) == emoji_lol:
            role = discord.utils.find(lambda r: r.name == "LoL", msg.guild.roles)
            await user.add_roles(role)
            print("Cargo adicionado com sucesso!")
        if str(reaction.emoji) == emoji_apex:
            role = discord.utils.find(lambda r: r.name == "Apex", msg.guild.roles)
            await user.add_roles(role)
            print("Cargo adicionado com sucesso!")

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'Bem vindo, gamer {member.mention}. Tudo bem!? (digite "ola")'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = '!',intents = intents)


client = MyClient(intents = intents)
client.run('MTAyNTE5MDczMzU3OTMwNTA3NA.GDgj98.aGekKxsLpr4dSOnuOH7BtNCcO2c4ENAzozyuO4')

