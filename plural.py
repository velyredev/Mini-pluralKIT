import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)


# Diccionario para guardar alters por usuario
alters_por_usuario = {}

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def add(ctx, nombre_alter): 
    author_id = str(ctx.author.id)

    # Comando para añadir un alter o personaje

    if not nombre_alter:
        await ctx.send("Por favor, escribe un nombre válido para el alter.")


        # Si el usuario no tiene una lista todavía, crearla
    if author_id not in alters_por_usuario:
        alters_por_usuario[author_id] = []

        alters_por_usuario[author_id].append(nombre_alter)
        await ctx.send(f"✨ Alter '{nombre_alter}' añadido a tu sistema, {ctx.author.name}.")
    else:
        alters_por_usuario[author_id].append(nombre_alter)
        await ctx.send(f"✨ Alter '{nombre_alter}' añadido a tu sistema, {ctx.author.name}.")


    # Comando para mostrar los alters del usuario
@bot.command()
async def mostrar(ctx):
    author_id = str(ctx.author.id)

    if author_id not in alters_por_usuario or not alters_por_usuario[author_id]:
            await ctx.send("No tienes alters añadidos aún. Usa `!add NOMBRE` para añadir uno.")
            

    lista = "\n".join(f"- {nombre}" for nombre in alters_por_usuario[author_id])
    await ctx.send(f"🧠 Tus alters registrados son:\n{lista}")



@bot.command()
async def remove(ctx, nombre_alter):
    author_id = str(ctx.author.id)

    if not nombre_alter:
        await ctx.send("Por favor, escribe un nombre válido para el alter.")


        # Si el usuario no tiene una lista todavía, crearla
    if author_id not in alters_por_usuario:
        alters_por_usuario[author_id] = []

        alters_por_usuario[author_id].remove(nombre_alter)
        await ctx.send(f"✨ Alter '{nombre_alter}' removido de tu sistema, {ctx.author.name}.")
    else:
        alters_por_usuario[author_id].remove(nombre_alter)
        await ctx.send(f"✨ Alter '{nombre_alter}' removido de tu sistema, {ctx.author.name}.")


    
# Reemplaza por tu token real
bot.run("REEMPLAZA POR UN TOKEN")
