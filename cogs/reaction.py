from discord.ext import commands
import discord
import random

# A list with links to reaction gifs (kiss, hug, punch and etc)
kis = ['https://cdn.discordapp.com/attachments/906658774935302227/909129371325960232/anime-kissing.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/916725599513485382/giphy3.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/916725599752564776/giphy2.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/916725600041984121/giphy.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/909129370357092382/anime-kiss3.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/909129373523804190/anime-kissing2.gif'
        ]


fuk = ['https://cdn.discordapp.com/attachments/1001737508205375558/1008126551474319432/ezgif.com-gif-maker.gif',
       'https://cdn.discordapp.com/attachments/1001737508205375558/1008128345336197160/ezgif.com-gif-maker.gif',
       'https://cdn.discordapp.com/attachments/1001737508205375558/1008130412196929607/ezgif.com-gif-maker.gif'
        ]

pats = ['https://media.discordapp.net/attachments/1003002531024228352/1008363607215591434/a9c771e756e3a920c0923a109f32c145.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363607538540594/b459058ae02cb62ce92c30f5be117928.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363678929784832/bf5be90f6800273b85b887e708c3815e.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363679349223434/e83745f1c57217d93d815a47f5e41664.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363679688958032/3b5e3cff6d5d1dfda13ec15ee1a248fc.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363780335468544/0d9b17b4b0cc7cfe6cc00373528e9474.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363780637470720/97461250280374af0819754a78900489.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363780960436244/e58320c0b6994fbba5448ad189d0c509.gif'
        ]

evill = ['https://media.discordapp.net/attachments/1003002531024228352/1008124195235975168/facf4a97d923e61f75e0a0aeb6e9df6d.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008124195651190955/df6cdb98409ee284ba1dd7dafd0b54a3.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008124268086829157/fa8a9aaa292f7a52b433ab879ce43451.gif'
        ]

hgs = ['https://media.discordapp.net/attachments/776936060298854431/1008779542845993040/hug-anime.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1008779543164751962/dc53bef31455468fbc3d5bff6afb1bdb.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1008779543466737825/kitsune-upload-hug.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1008779543785517056/428b7ed57db9d7aeb2e3f70f21f7bb25.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1008779544104276121/anime-hug-40.gif'
        ]



class Reaction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    emb1 = discord.Embed(color=member.color, title="Ошибка")
    emb1.description = f"Вы не указали участника."



    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="Поцелуй")
        embed.description = f"{ctx.author.mention} Поцеловал(а) {member.mention}"
        url = (random.choice(kis))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def fuck(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="СЕКС")
        embed.description = f"{ctx.author.mention} Трахнул(а) {member.mention}"
        url = (random.choice(fuk))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="Поглаживание")
        embed.description = f"{ctx.author.mention} Погладил(a) {member.mention}"
        url = (random.choice(pats))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def evillaugh(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="Злой смех")
        embed.description = f"{ctx.author.mention} Злобно смеётся"
        url = (random.choice(evill))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(emb1=embed)
        embed = discord.Embed(color=member.color, title="Обнимашки")
        embed.description = f"{ctx.author.mention} Обнял(а) {member.mention}"
        url = (random.choice(hgs))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Reaction(bot))