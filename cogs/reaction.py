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


cr = ['https://media.discordapp.net/attachments/1008837483854839931/1008837646098907239/a5d003d3f67045f74a27af43b7d58cc3.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008837646715465758/15e6665e081b25f568b9862c3e44bca0.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008837645469765662/a58f3913f982fc4bf4e312bcfd52ab56.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008837621507698719/b10ef406caf27fe40bd7b48601159f62.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008837621214089316/8e6c988405be881d71dd45f87934d623.gif',
        'https://cdn.discordapp.com/attachments/1008837483854839931/1008837680001470565/3b939ff5e455740ec474494e4d3d9943.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008837680412500139/e8a4bf9ff50e7a29a822e957ba4d604d.gif'
        ]


sml = ['https://media.discordapp.net/attachments/1008837483854839931/1008840866137387018/da8f1b48d16217743b7db3b878893d59.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840866519056404/1c3f4ba375426170d8c4dcf5744d5b1b.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840866980450304/2266fc48dfc7fdfbe6f9d6f82e014236.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840907988144189/dac7329b53246ab7d0494d68f83882f4.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840908344664144/cd6d7d8baa42d7b656b569f0857a9a7f.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840908747313294/031d5a23aff020ae4a5842e326aad4d4.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840940754063370/1a0705b89247c5052ea0a26c15a27ae2.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008840941416759347/a5ad2e982003ce4dc18bf59621d11d3c.gif']


fp = ['https://media.discordapp.net/attachments/1008837483854839931/1008844012360319136/eb10f3b3011dce02.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008844012679082044/fap-cartoon.gif',
        'https://media.discordapp.net/attachments/898627420956012584/1008852145266757792/45eecd6154ba228157ee646bb15043453f430524_hq.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008845730213011506/chuunibyou-fap.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008845730523385866/48282f5910780b8e41a88ea289a44a52.gif']


smg = ['https://media.discordapp.net/attachments/1008837483854839931/1008847791478554734/615dddaec92b2bd6750fb46f4272457c.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008847792166424677/9d2248252f6d9e7dfd223e993cfeff32.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008847791809888316/db43381b262226fad2c89a3db5a9b317.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008847804854186155/9cb145cb781925995311c74aef5d9bca.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008847805210689718/878f5e5cb978c30b93e46f4b1729b5b2.gif']


angr = ['https://media.discordapp.net/attachments/1008837483854839931/1008849362387992698/e97da887a8968dbbd4a5af24ad8115ae.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008849362815823983/3ffadf809983f553445ee3d0ff553044.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008849363231051786/9b5a9f597b692baa842e597e67e698e1.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008849400174485626/9cd01eaed3df7f00a047df94b7252b51.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008849400568762428/2b9d797fbb3c02d7f2ca66a407dbeaca.gif']


wnk = ['https://media.discordapp.net/attachments/1008837483854839931/1008852217241010186/97c6cbaf7696d81ea3598d9f6149896a.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008852217656254576/8e587b78a37f012e99c4ab7c2f4e81bf.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008852218012766218/0ae6c4ff3742a1f98bc8160ee86af905.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008852261172166746/56cc7d9993b7e9315e2374765cf2caa4.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008852261520277695/08b10d500cc4ee1636c5a01cbbd5b357.gif',
        'https://media.discordapp.net/attachments/1008837483854839931/1008852261864226856/62bfba79874e765af7ab0f463e811922.gif']


kll = ['https://media.discordapp.net/attachments/776936060298854431/1009025471092097064/yuno-gasai-gif-16.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009025471482179664/58fdc8ad8454253ea1982cd6f79fe184.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009025471813521559/anime-death.gif']

pok = ['https://media.discordapp.net/attachments/776936060298854431/1009027011030831134/poke-anime_1.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009027011508969502/poke-anime.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009027011894841394/CYxJyxQ.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009027012305895454/S00v.gif']

slp = ['https://media.discordapp.net/attachments/776936060298854431/1009028559207153684/girl-slap.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009028559655927808/B2Sm.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009028560234754098/BQM6jEZ-UJLgGUuvrNkYUHEZ_33p1we3TqZWmyZ6XW6iZ0m7dzGNimq8VUNzJkvR6yYwbx8kQMqR2_6m-cFJwA.gif',
        'https://media.discordapp.net/attachments/776936060298854431/1009028560704503848/1c8f0f43c75c11bf504b25340ddd912d.gif']


class Reaction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))



    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Поцелуй")
        embed.description = f"{ctx.author.mention} **Поцеловал(а)** {member.mention}"
        url = (random.choice(kis))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def fuck(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="СЕКС")
        embed.description = f"{ctx.author.mention} **Трахнул(а)** {member.mention}"
        url = (random.choice(fuk))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Поглаживание")
        embed.description = f"{ctx.author.mention} **Погладил(a)** {member.mention}"
        url = (random.choice(pats))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def evillaugh(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Злой смех")
        embed.description = f"{ctx.author.mention} **Злобно смеётся**"
        url = (random.choice(evill))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Обнимашки")
        embed.description = f"{ctx.author.mention} **Обнял(а)** {member.mention}"
        url = (random.choice(hgs))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def cry(self, ctx, member: discord.Member = None):
        embed = discord.Embed(title="Плач")
        embed.description = f"{ctx.author.mention} **Громко рыдает**"
        url = (random.choice(cr))
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    
    @commands.command()
    async def smile(self, ctx, member: discord.Member = None):
        embed = discord.Embed(title="Улыбашки")
        embed.description = f"{ctx.author.mention} **Широко улыбаеться**"
        url = (random.choice(sml))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def fap(self, ctx, member: discord.Member = None):
        embed = discord.Embed(title="Дрочка")
        embed.description = f"{ctx.author.mention} **Жёстко наяривает**"
        url = (random.choice(fp))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def smug(self, ctx, member: discord.Member = None):
        embed = discord.Embed(title="Улыбашки")
        embed.description = f"{ctx.author.mention} **Самодовольно Улыбаеться**"
        url = (random.choice(smg))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def angry(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Злюка")
        embed.description = f"{ctx.author.mention} **Злится на** {member.mention}"
        url = (random.choice(angr))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def wink(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Подмигивание")
        embed.description = f"{ctx.author.mention} **Подмигинул** {member.mention}"
        url = (random.choice(wnk))
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Убийство")
        embed.description = f"{ctx.author.mention} **Убил** {member.mention}"
        url = (random.choice(kll))
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Тычка")
        embed.description = f"{ctx.author.mention} **Тыкнул** {member.mention}"
        url = (random.choice(pok))
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Вы не указали участника")
        embed = discord.Embed(title="Пощёчина")
        embed.description = f"{ctx.author.mention} **Дал(а) пощёчину** {member.mention}"
        url = (random.choice(slp))
        embed.set_image(url=url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Reaction(bot))