from discord import errors
from discord.ext import commands
import requests
import json 
from modules.Search import queryAnime
from utils.helpers import quick_embed


class ani(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
        #print(animeName)
        variables = {
            'name': animeName
        }

        url = 'https://graphql.anilist.co'
    # Make the HTTP Api request
        response = requests.post(url, json={'query': query, 'variables': variables})
        response = json.loads(response.text)
        try:
            color = int(hex(int(str(response['data']['Media']['coverImage']['color']).replace("#", ""), 16)), 0)
        except ValueError:
            print('color error has been caught')
            color = 16777215 
        try:
            banner = response['data']['Media']['bannerImage']
            if(banner is None):
                raise Exception
        except Exception:
            print("banner is unavailable")
            banner = 'https://i.pinimg.com/originals/05/0f/0a/050f0a3bd19ce811522f0c63256637e9.jpg'
            

        embedDescription = "**Average Score: "+ str(response['data']['Media']['averageScore'])+ "\nSeason: "+ str(response['data']['Media']['season']).capitalize()+" "+str(response['data']['Media']['seasonYear']) + "\nPopularity: "+ str(response['data']['Media']['popularity']) +"\nStatus: "+ str(response['data']['Media']['status']).capitalize() + "\nGenres: " + str(response['data']['Media']['genres'])[1:-1].replace("'","") + "**\n"+ "\n"+(response['data']['Media']['description']).replace('<br>','').replace('<b>','').replace('</b>','')
        await quick_embed(
            ctx,
            title = str(response['data']['Media']['title']['english']) +" ("+ str(response['data']['Media']['title']['native']) +")",
            description= embedDescription,
            color= color,
            thumbnail = str(response['data']['Media']['coverImage']['extraLarge']),
            image_url = banner,
        )
        
    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def charSearch(self, ctx,*, charName):
        await ctx.send("monkey")


def setup(bot):
    bot.add_cog(ani(bot))
