import telebot
from chatterbot import ChatBot

bot = telebot.TeleBot("825106070:AAFjXRJkvxa3O9bcoAJd1Ip4YsrQ6lHPpe8")

def bot_conversacional(message):

	chatbot = ChatBot ("Ejemplo de bot",trainer = "chatterbot.trainers.ChatterBotCorpusTrainer")
	respuesta = chatbot.get_response(message)
	respuesta = str(respuesta)
	mensaje= open("respuesta.txt", "w")
	mensaje.write(respuesta)
	mensaje.close()


@bot.message_handler(commands = ["help", "start"])#recibimos y enviamos respuesta
def enviar_mensaje(message):
	bot.reply_to(message,"Hola,estoy aqui para resolver tus dudas")

@bot.message_handler(func=lambda message:True)
def mensaje(message):																																		
	bot_conversacional(message.text)
	respuesta=open("respuesta.txt", "r")					
	respuesta=respuesta.read()
	bot.reply_to(message, respuesta)
bot.polling()


