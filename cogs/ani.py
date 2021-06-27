import os
import discord 
from discord.ext import commands
import asyncio
import json
import requests
from modules.Search import queryAnime
from utils.helpers import quick_embed

class ani(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Python Bot is now online")




    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! **{round(self.client.latency *1000)}ms**')





    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def aniSearch(self,ctx, *, animeName):
        query = await queryAnime()
        print(animeName)
        variables = {
            'name': animeName
        }

        url = 'https://graphql.anilist.co'
    # Make the HTTP Api request
        response = requests.post(url, json={'query': query, 'variables': variables}).json()
        color = 16777215
        print(response.get('season'))
        if (response['data']['Media']['coverImage']['color'] is not None):
            color = int(hex(int(str(response['data']['Media']['coverImage']['color']).replace("#", ""), 16)), 0)
        
        embedDescription = "**Average Score: "+ str(response['data']['Media']['averageScore'])+ "**" + "\n**Season: "+ str(response['data']['Media']['season']).capitalize()+" "+str(response['data']['Media']['seasonYear']) + "**"+ "\n**Popularity: "+ str(response['data']['Media']['popularity']) + "**"+"\n**Status: "+ str(response['data']['Media']['status']).capitalize() + "**\n"+ "\n"+(response['data']['Media']['description']).replace('<br>','').replace('<b>','').replace('</b>','')
        await quick_embed(
            ctx,
            title = str(response['data']['Media']['title']['english']) +" ("+ str(response['data']['Media']['title']['native']) +")",
            description= embedDescription,
            color= color,
            thumbnail = str(response['data']['Media']['coverImage']['extraLarge']),
            image_url = str(response['data']['Media']['bannerImage']),
        )
        
def setup(client):
    client.add_cog(ani(client))
