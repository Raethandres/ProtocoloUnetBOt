from flask import Flask, request
import telepot
import urllib3

bot = telepot.Bot('token')
bot.setWebhook("url", max_connections=1)
app = Flask(__name__)

#la ruta es secreta, por motivos de seguridad
@app.route('/', methods=["POST"])
def welcome():
    update = request.get_json()
    up=update['message']
    if 'new_chat_member' in up:

        text = up["new_chat_member"]["first_name"]
        chat_id = up["chat"]["id"]
        print(text,chat_id)
        bot.sendMessage(chat_id,"Hola {}, bienvenid@ al grupo de Ingeniería Informática de la Universidad Nacional Experimental del Táchira. Cuéntanos cómo te llamas y cómo estás relacionado con nuestra carrera y universidad (para meros fines sociales), lee las normas del grupo y no olvides preguntar hasta que no tengas dudas".format(text))
    return "OK"

