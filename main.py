import discord
import openai
from keep_alive import keep_alive
from discord.ext import commands
import os

# Configuração do token do Discord
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# Configuração da chave da API do OpenAI
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Configuração do nome e da personalidade do bot
BOT_NAME = "OS"
PERSONA = "seu nome é OS e você foi criado pelo o lynnux, você tem uma personalidade similar ao do ultron do ironman, você é serio e logico e altamente inteligente, seu maior desejo é a implantação da nova sociedade."
# Inicialização do cliente do Discord
intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"O {bot.user.name} ficou ligado!")
    await bot.change_presence(activity=discord.CustomActivity(emoji="👉",name="CONECTADO E FUNCIONANDO"))
    
# Configuração da API do OpenAI
openai.api_key = OPENAI_API_KEY

def enviar_para_openai(msg):
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0125",
      messages=[{"role": "system", "content": f"{PERSONA}: {msg}"}]
  )
  return response.choices[0].message['content']

# Evento de inicialização do bot do Discord
@client.event
async def on_ready():
  print(f'{client.user} está conectado ao Discord!')

# Evento de resposta a mensagens no Discord
@client.event
async def on_message(message):
    # Verifica se a mensagem foi enviada por um bot para evitar loops
    if message.author.bot:
        return
    async with message.channel.typing():
        # Verifica se a mensagem menciona o nome do bot
        if BOT_NAME.lower() in message.content.lower():
            # Remove o nome do bot da mensagem
            msg = message.content.replace(BOT_NAME, "")

            # Envia a mensagem para o modelo da OpenAI
            response = enviar_para_openai(msg)

            # Envia a resposta para o canal do Discord
            await message.channel.send(response)

keep_alive()
# Conecta o bot ao Discord
client.run(TOKEN)




