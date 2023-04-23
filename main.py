import logging
import requests
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, Update, Document
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackQueryHandler, CallbackContext, filters, MessageHandler
from telegram import CallbackQuery
from threading import Timer
from telegram.ext import ParseMode
import time
import random
import string
import emoji
from io import BytesIO
from platform import python_version
# Configuración de registro de logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Token del bot de Telegram
TOKEN = '5516270858:AAHEeuC46ozoOczZgrRM7n8ocVytmxqs8vs'


def start_command(update, context):
    query = update.message.text  # Obtén el texto del comando /start
    user_id = update.message.chat_id
    
    # Crea los botones con callback_data
    button1 = InlineKeyboardButton(text='Info 🍏', callback_data='boton1')
    # Crea el markup del teclado inline
    reply_markup = InlineKeyboardMarkup([[button1]])
    
    # Envía un gif con texto y botones en una misma respuesta
    context.bot.send_animation(
        chat_id=user_id,
        animation='https://media2.giphy.com/media/WOb8EeFziTQNE02WXs/giphy.gif?cid=ecf05e47j8ecgx9vil5gs6had3krzhjzd8jbyzg4llv9ng2e&rid=giphy.gif&ct=g',  # URL del gif
        caption='Hola, no te puedo ayudar mucho.',
        reply_markup=reply_markup
    )







############################################################################################################################################
############################################################################################################################################

def is_premium_user(user_id):
    with open("premium.txt", "r") as file:
        premium_users = [int(line.strip()) for line in file]
    return user_id in premium_users

############################################################################################################################################
############################################################################################################################################

def bin_command(update, context):
    user_id = update.effective_user.id
    # Verificar si el usuario es premium
    if not is_premium_user(user_id):
        # Si no es premium, enviar un mensaje de error
        return update.message.reply_text("Lo siento, solo los usuarios premium pueden usar este servicio.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Seller 🧸", url="https://t.me/hackerismyname"), InlineKeyboardButton("finalizar 🍎", callback_data="fin2")]]))
    
    BIN = update.message.text[len("/bin"): 11]

    # Crea los botones con callback_data
    button2 = InlineKeyboardButton(text='finalizar 🍎', callback_data='fin2')
    # Crea el markup del teclado inline
    reply_markup = InlineKeyboardMarkup([[button2]])
    

    if len(BIN) < 7:
        return update.message.reply_text("<b>• 𝗨𝘀𝗮𝗿 <code>/bin 456789</code></b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    if not BIN:
        return update.message.reply_text("<b>• 𝗨𝘀𝗮𝗿 <code>/bin 456789</code></b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    inputm = update.message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]
    req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
    if 'bin' not in req:
        return update.message.reply_text(f'<b>• 𝗕𝗶𝗻 ➻ no encontrado <code>{BIN} ❌</code></b>', reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    else:
        brand = req['brand']
        country = req['country']
        country_name = req['country_name']
        country_flag = req['country_flag']
        country_currencies = req['country_currencies']
        bank = req['bank']
        level = req['level']
        typea  = req['type']

        return update.message.reply_text(f"""
       <b>
• 𝗕𝗶𝗻   <code>{BIN}</code>
<b>{country}  |  {country_flag}  |  {country_name}</b>
╔════════<b> Details </b>════════╗
<b> ➻ Status = 𝑨𝒑𝒓𝒐𝒗𝒂𝒅𝒐 ✅</b>
<b> ➻ Data</b> ⇾ {brand} - {typea} - {level}
<b> ➻ Bank</b> ⇾  {bank}
╚═════════ ♤ ═════════╝
Owner <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b>
</b>
        """, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

#################################################################################################################################
#################################################################################################################################


# Lista para almacenar los usuarios registrados
registered_users = []

# Función para manejar el comando /register
def register(update, context):
    # Obtener el ID del usuario que envió el comando
    user_id = update.message.from_user.id
    # Crea los botones con callback_data
    button3 = InlineKeyboardButton(text='finalizar 🍎', callback_data='fin2')
    # Crea el markup del teclado inline
    reply_markup = InlineKeyboardMarkup([[button3]])
    # Verificar si el usuario ya está registrado
    if str(user_id) in registered_users:
        update.message.reply_text("Ya estás registrado.")
    else:
        # Registrar al usuario en la lista de usuarios registrados
        registered_users.append(str(user_id))
        with open('usuarios.txt', 'a') as archivo:
            archivo.write(str(user_id) + '\n')
        update.message.reply_text("¡Te has registrado exitosamente!", reply_markup=reply_markup)










def userlist(update, context):
    button4 = InlineKeyboardButton(text='Seller 🧸', url='t.me/hackerismyname')
    reply_markup = InlineKeyboardMarkup([[button4]])
    # Obtener el ID del usuario que envió el comando
    user_id = update.message.from_user.id
    
    # Verificar si el ID del usuario coincide con el ID del creador
    if user_id == 1787128910:  # Reemplazar con el ID de usuario del creador
        with open('usuarios.txt', 'r') as archivo:
            chats = archivo.readlines()
        chatfile = "Esta es la lista de los usuarios registrados de @WeekndChk_bot.\n\n"
        P = 1
        for chat in chats:
            try:
                chatfile += "{} : {}\n".format(P, chat)
                P = P + 1
            except:
                pass
        with BytesIO(str.encode(chatfile)) as output:
            output.name = "Usuarios Registrados.txt"
            update.message.reply_document(document=output, caption="Lista de Usuarios Registrados",
                                          disable_notification=True)
    else:
        update.message.reply_text("Lo siento, este comando solo puede ser utilizado por el creador del bot.", reply_markup=reply_markup)









#################################################################################################################################
#################################################################################################################################


def key_command(update: Update, context: CallbackContext):
    admins = ['1787128910']  # Lista de IDs de administradores
    if str(update.effective_user.id) in admins:
        data = update.message.text.split(" ", 2)
        if len(data) < 2:
            update.message.reply_text("<b>• 𝗨𝘀𝗮𝗿 <code>/key dias-id-credit</code></b>", parse_mode=ParseMode.HTML)
            return

        ccs = data[1]
        card = ccs.split("-")
        dia = card[0]
        user = card[1]
        cre = card[2]

        key = 'hackerbotchk_' + str(random.randint(1000, 9000)) + '-' + f'{user}' + '_' + f'{cre}'
        print(key)
        key1 = 'hackerbotchk-' + str(random.randint(1000, 9000)) + '-' + str(random.randint(1000, 9000))
        print(key1)
        # Escribir la key en el archivo keys.txt
        with open(file='keys.txt', mode='a', encoding='utf-8') as archivo:
            archivo.write('{}\n\n'.format(key))
        text = f"""<b>
• 𝗞𝗲𝘆 𝗨𝘀𝗲𝗿
―――――――
<b> ➻ Key =</b> Key Aprovada ✅
<b> ➻ Creditos :</b> <Code>{cre}</code>
<b> ➻ Id :</b> <code>{user}</code>
<b> ➻ Dias :</b> <code>{dia}</code>
╔════════<b> Key </b>════════╗

<code>{key}</code> 

╚═════════ ♤ ═════════╝
Owner <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b></b>"""
        # Enviar la foto y el texto como respuesta al mensaje
        update.message.reply_photo("https://imgur.com/Xt7OdE7", caption=f'{text}', parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CLAIM  🏆 ", url="https://t.me/WeekndChk_bot")]]))

    else:
        update.message.reply_text('<b>⎚Este comando es solo para administradores</b>', parse_mode=ParseMode.HTML)







def key_command1(update: Update, context: CallbackContext):
    admins = ['1787128910']  # Lista de IDs de administradores
    if str(update.effective_user.id) in admins:
        data = update.message.text.split(" ", 2)
        if len(data) < 2:
            update.message.reply_text("<b>• 𝗨𝘀𝗮𝗿 <code>/genkey dias</code></b>", parse_mode=ParseMode.HTML)
            return

        ccs = data[1]
        card = ccs.split("-")
        dia = card[0]

        key1 = 'jokerchk-' + str(random.randint(1000, 9000)) + '-' + str(random.randint(1000, 9000))
        print(key1)
        # Escribir la key en el archivo keys.txt
        with open(file='keyspremium.txt', mode='a', encoding='utf-8') as archivo:
            archivo.write('{}\n\n'.format(key1))
        text = f"""<b>
• 𝗞𝗲𝘆 𝗨𝘀𝗲𝗿
―――――――
<b> ➻ Key =</b> Key Aprovada ✅
<b> ➻ Status :</b> <code>Premium</code>
<b> ➻ Dias :</b> <code>{dia}</code>
╔════════<b> Key </b>════════╗

<code>{key1}</code> 

╚═════════ ♤ ═════════╝
Owner <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b></b>"""
        # Enviar la foto y el texto como respuesta al mensaje
        update.message.reply_photo("https://pbs.twimg.com/media/FW_sRzzXoAM90G-.jpg:large", caption=f'{text}', parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CLAIM  🏆 ", url="https://t.me/WeekndChk_bot")]]))

    else:
        update.message.reply_text('<b>• Este comando es solo para administradores.</b>', parse_mode=ParseMode.HTML)
####################################################################################################################
####################################################################################################################

FILE_PATH = "keyspremium.txt"

# Función para manejar el comando /claim
def claim_key(update, context):
    user_id = update.message.from_user.id

    with open(file='usuarios.txt', mode='r+', encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(user_id) + '\n' in x:
            zipcode = update.message.text[len('/claim '):]

            if len(zipcode) < 2:
                update.message.reply_text("<b>• 𝗨𝘀𝗮𝗿 <code>/claim jokerchk-xxxx-xxxxx</code></b>", parse_mode=ParseMode.HTML)
                return
            if not zipcode:
                update.message.reply_text("<b>• 𝗨𝘀𝗮𝗿 <code>/claim jokerchk-xxxx-xxxxx</code></b>", parse_mode=ParseMode.HTML)
                return

            with open(FILE_PATH, "r") as f:
                keys = f.read().splitlines()

            key = keys.pop(random.randint(0, len(keys)-1))
            print(key+' aprovada')

            if len(keys) == 0:
                update.message.reply_text("<b>• Key 𝐑𝐞𝐜𝐥𝐚𝐦𝐚𝐝𝐚!</b>", parse_mode=ParseMode.HTML)
                return

            with open(FILE_PATH, "w") as f:
                f.write("\n".join(keys))

            with open(file='premium.txt', mode='r+', encoding='utf-8') as archivo:
                x = archivo.readlines()

                archivo.write('{}\n'.format(user_id))

            text = f"""<b>
• 𝗣𝗹𝗮𝗻 𝗣𝗿𝗲𝗺𝗶𝘂𝗺
<b>Status:</b>   Key Aprovada ✅
╔════════<b> Premium </b>════════╗
<b> ➻ Key:</b>   <code>• 𝐑𝐞𝐜𝐥𝐚𝐦𝐚𝐝𝐚!</code>
<b> ➻ Usuario:</b>   <code>{update.message.from_user.first_name} </code>
<b> ➻ ID:</b>   <code>{user_id}</code>
<b> ➻ Plan:</b>   𝙋𝙧𝙚𝙢𝙞𝙪𝙢 🏆
╚═════════ ♤ ═════════╝
Creado por <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b>
    </b>"""
            context.bot.send_photo(chat_id=update.message.chat_id, photo="https://pbs.twimg.com/media/E_HyLqaVIAAH8vJ.jpg", caption=text, parse_mode=ParseMode.HTML)

        else:
            update.message.reply_text(f'<b>• 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝘁𝗲 <code>/register</code></b>', parse_mode=ParseMode.HTML)










####################################################################################################################
####################################################################################################################

# Función de manejo del comando /me, /yo, /my, /myacc
def my_command(update, context):
    user = update.message.from_user.first_name
    user_id = update.message.from_user.id
    seller = [1787128910]
    admin = [1787128911]

    if user_id in seller or user_id in seller:
        message = f"""<b>
• 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶ó𝗻 𝗱𝗲𝗹 𝗨𝘀𝘂𝗮𝗿𝗶𝗼
╔════════<b> Owner </b>════════╗
<b> ➻ Nombre:</b>   <code>{user}</code>
<b> ➻ ID:</b>   <code>{user_id}</code>
<b> ➻ Créditos:</b>   <code>9999</code>
<b> ➻ Estado:</b>   <code>CREADOR 🥀</code>
<b> ➻ Plan:</b>   𝘿𝙄𝘼𝙈𝘼𝙉𝙏𝙀 🐯
╚═════════ ♤ ═════════╝
Creado por <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b>
    </b>"""
    elif user_id in admin:
        message = f"""<b>
• 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶ó𝗻 𝗱𝗲𝗹 𝗨𝘀𝘂𝗮𝗿𝗶𝗼
╔════════<b> Admin </b>════════╗
<b> ➻ Nombre:</b>   <code>{user}</code>
<b> ➻ ID:</b>   <code>{user_id}</code>
<b> ➻ Estado:</b>   <code>Pro 🥇</code>
<b> ➻ Plan:</b>   𝙑𝙄𝙋 👑
╚═════════ ♤ ═════════╝
Creado por <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b>
    </b>"""
    else:
        with open(file='premium.txt', mode='r+', encoding='utf-8') as archivo:
            x = archivo.readlines()
            if str(user_id) + '\n' in x:
                message = f"""<b>
• 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶ó𝗻 𝗱𝗲𝗹 𝗨𝘀𝘂𝗮𝗿𝗶𝗼
╔════════<b> Premium </b>════════╗
<b> ➻ Nombre:</b>   <code>{user}</code>
<b> ➻ ID:</b>   <code>{user_id}</code>
<b> ➻ Estado:</b>   <code>Money 🤑</code>
<b> ➻ Plan:</b>   𝙋𝙧𝙚𝙢𝙞𝙪𝙢 🏆
╚═════════ ♤ ═════════╝
Creado por <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b>
            </b>"""
            else:
                message = f"""<b>
• 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶ó𝗻 𝗱𝗲𝗹 𝗨𝘀𝘂𝗮𝗿𝗶𝗼
╔════════<b> Free </b>════════╗
<b> ➻ Nombre:</b>   <code>{user}</code>
<b> ➻ ID:</b>   <code>{user_id}</code>
<b> ➻ Estado:</b>   <code>Podrido 🪰</code>
<b> ➻ Plan:</b>   𝙁𝙍𝙀𝙀 💩
╚═════════ ♤ ═════════╝
Creado por <b><a href="tg://resolve?domain=hackerismyname">𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱</a></b>
            </b>"""
    update.message.reply_text(text=message, parse_mode='HTML')

#################################################################################################################
#################################################################################################################

# Lista de usuarios premium
def obtener_usuarios_premium():
    with open("premium.txt", "r") as file:
        usuarios_premium = [int(line.strip()) for line in file]
    return usuarios_premium
# Función para generar correo temporal
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena
def generar_correo_temporal(update, context):
    user_id = update.effective_user.id
    usuarios_premium = obtener_usuarios_premium()
    longitud = 8
    contrasena_generada = generar_contrasena(longitud)
    if user_id in usuarios_premium:
        dominios = ['@lieboe.com', '@xywdining.com', "@nefyp.com", "@pihey.com"]  # Cambia esto al dominio de correo temporal que desees
        longitud_nombre = random.randint(7, 10)  # Cambia esto a la longitud deseada para el nombre de usuario del correo
        caracteres_validos = string.ascii_letters + string.digits  # Caracteres válidos para el nombre de usuario del correo
        nombre_usuario = ''.join(random.choice(caracteres_validos) for _ in range(longitud_nombre))
        dominio = random.choice(dominios)
        correo_temporal = nombre_usuario + dominio
        # Enviar el correo generado como respuesta al comando /mail
        context.bot.send_message(chat_id=update.effective_chat.id, text="""
• 𝗖𝗼𝗿𝗿𝗲𝗼 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗹 𝗴𝗲𝗻𝗲𝗿𝗮𝗱𝗼
╔════════<b> Mail </b>════════╗

 ➻ 𝗠𝗮𝗶𝗹: <code>{}</code>

 ➻ 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱: <code>{}</code>

╚═════════ ♤ ═════════╝
Owner 𝙝𝙖𝙘𝙠𝙚𝙧 🇨🇱""".format(correo_temporal, contrasena_generada), parse_mode=ParseMode.HTML)
    else:
        # Enviar mensaje de error si el usuario no es premium
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, solo los usuarios premium pueden usar este servicio.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Seller 🧸", url="https://t.me/hackerismyname"), InlineKeyboardButton("finalizar 🍎", callback_data="fin2")]]))


##########################################################################################################################################
##########################################################################################################################################

def generate_cards(update, context):
    # Iniciar el estado de "typing"
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    start_time = time.time()
    time.sleep(0.1)  # Simular proceso de generación de tarjetas
    # Obtener los 6 primeros dígitos proporcionados por el usuario
    user_input = context.args[0] if context.args else None
    if user_input and user_input.isdigit() and len(user_input) >= 6:
        # Generar 10 tarjetas de crédito válidas basadas en los 6 primeros dígitos
        cards = [generar_tarjeta(user_input) for _ in range(10)]
        # Unir las tarjetas de crédito en una cadena con saltos de línea y formato de código
        cards_string = "\n".join([f"<code>{card}</code>" for card in cards])
        # Crear botón para regenerar las tarjetas
        keyboard = [[InlineKeyboardButton("𝗢𝘄𝗻𝗲𝗿 🐯", url='t.me/hackerismyname')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Obtener la información del BIN
        bin_info = get_bin_info(user_input)
        # Enviar la respuesta al usuario
        end_time = time.time()
        response_time = end_time - start_time
        update.message.reply_text(f"• 𝗚𝗲𝗻𝗲𝗿𝗮𝗱𝗮𝘀 🍏\n• 𝗧𝗶𝗺𝗲 {response_time:.3f}'s\n╔════════<b> 𝑪𝑪s </b>════════╗\n{cards_string}\n╔════════<b> 𝑫𝒆𝒕𝒂𝒍𝒍𝒆𝒔 </b>═══════╗\n{bin_info}\n╚═════════ ♤ ═════════╝\n", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text("Por favor, proporciona los 6 primeros dígitos de una tarjeta de crédito válida.")

def validar_tarjeta(card_number):
    card_digits = [int(d) for d in card_number]
    check_digit = card_digits.pop()

    card_digits.reverse()
    for i in range(0, len(card_digits), 2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9

    return (sum(card_digits) + check_digit) % 10 == 0

def generar_tarjeta(user_input):
    # Obtener la cantidad de dígitos proporcionados por el usuario
    num_digits = len(user_input)
    # Calcular cuántos dígitos faltan para completar 16 dígitos
    num_missing_digits = 15 - num_digits
    # Generar los dígitos faltantes aleatoriamente
    missing_digits = "".join(random.choice("0123456789") for _ in range(num_missing_digits))
    # Concatenar los dígitos proporcionados por el usuario y los dígitos aleatorios para formar el número de tarjeta de crédito
    card_number = user_input + missing_digits

    # Generar el dígito de verificación utilizando el algoritmo de Luhn
    card_digits = [int(d) for d in card_number]
    for i in range(len(card_digits) - 2, -1, -2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9
    checksum = sum(card_digits) % 10
    if checksum > 0:
        checksum = 10 - checksum

    # Combinar el dígito de verificación con el número de tarjeta de crédito completo
    card_number += str(checksum)

    # Verificar si el número de tarjeta de crédito generado es válido
    if validar_tarjeta(card_number):
        # Generar la fecha de vencimiento (MM/YY)
        expiration_month = str(random.randint(1, 12)).zfill(2)
        expiration_year = str(random.randint(2023, 2030))

        # Generar el CVV (Código de Verificación de Tarjeta) de 3 dígitos
        cvv = "".join(random.choice("0123456789") for _ in range(3))

        # Combinar el número de tarjeta de crédito con la fecha de vencimiento y el CVV
        card_with_expiration_and_cvv = f"{card_number}|{expiration_month}|{expiration_year}|{cvv}"
        return card_with_expiration_and_cvv

    # Si el número de tarjeta de crédito generado no es válido, volver a generar uno
    return generar_tarjeta(user_input)



# Tabla de códigos de país y sus respectivas banderas
COUNTRY_FLAGS = {
    "US": "🇺🇸",  # Estados Unidos
    "CA": "🇨🇦",  # Canadá
    "MX": "🇲🇽",  # México
    "GT": "🇬🇹",  # Guatemala
    "HN": "🇭🇳",  # Honduras
    "SV": "🇸🇻",  # El Salvador
    "NI": "🇳🇮",  # Nicaragua
    "CR": "🇨🇷",  # Costa Rica
    "PA": "🇵🇦",  # Panamá
    "CU": "🇨🇺",  # Cuba
    "DO": "🇩🇴",  # República Dominicana
    "HT": "🇭🇹",  # Haití
    "JM": "🇯🇲",  # Jamaica
    "PR": "🇵🇷",  # Puerto Rico
    "VE": "🇻🇪",  # Venezuela
    "CO": "🇨🇴",  # Colombia
    "EC": "🇪🇨",  # Ecuador
    "PE": "🇵🇪",  # Perú
    "BO": "🇧🇴",  # Bolivia
    "CL": "🇨🇱",  # Chile
    "PY": "🇵🇾",  # Paraguay
    "UY": "🇺🇾",  # Uruguay
    "AR": "🇦🇷",  # Argentina
    "BR": "🇧🇷",  # Brasil
    "CO": "🇨🇷",  # Costa Rica
    "VE": "🇻🇪",  # Venezuela
    "PE": "🇵🇪",  # Perú
    "EC": "🇪🇨",  # Ecuador
    "GY": "🇬🇾",  # Guyana
    "SR": "🇸🇷",  # Surinam
    "GF": "🇬🇫",  # Guayana Francesa
    "AD": "🇦🇩",  # Andorra
    "AL": "🇦🇱",  # Albania
    "AT": "🇦🇹",  # Austria
    "BA": "🇧🇦",  # Bosnia y Herzegovina
    "BE": "🇧🇪",  # Bélgica
    "BG": "🇧🇬",  # Bulgaria
    "BY": "🇧🇾",  # Bielorrusia
    "CH": "🇨🇭",  # Suiza
    "CY": "🇨🇾",  # Chipre
    "CZ": "🇨🇿",  # República Checa
    "DE": "🇩🇪",  # Alemania
    "DK": "🇩🇰",  # Dinamarca
    "EE": "🇪🇪",  # Estonia
    "ES": "🇪🇸",  # España
    "FI": "🇫🇮",  # Finlandia
    "FO": "🇫🇴",  # Islas Feroe
    "FR": "🇫🇷",  # Francia
    "GB": "🇬🇧",  # Reino Unido
    "GG": "🇬🇬",  # Guernsey
    "GI": "🇬🇮",  # Gibraltar
    "GR": "🇬🇷",  # Grecia
    "HR": "🇭🇷",  # Croacia
    "HU": "🇭🇺",  # Hungría
    "IE": "🇮🇪",  # Irlanda
    "IM": "🇮🇲",  # Isla de Man
    "IS": "🇮🇸",  # Islandia
    "IT": "🇮🇹",  # Italia
    "JE": "🇯🇪",  # Jersey
    "LI": "🇱🇮",  # Liechtenstein
    "LT": "🇱🇹",  # Lituania
    "LU": "🇱🇺",  # Luxemburgo
    "LV": "🇱🇻",  # Letonia
    "MC": "🇲🇨",  # Mónaco
    "MD": "🇲🇩",  # Moldavia
    "ME": "🇲🇪",  # Montenegro
    "MK": "🇲🇰",  # Macedonia del Norte
    "MT": "🇲🇹",  # Malta
    "NL": "🇳🇱",  # Países Bajos
    "NO": "🇳🇴",  # Noruega
    "PL": "🇵🇱",  # Polonia
    "PT": "🇵🇹",  # Portugal
    "IL": "🇮🇱",
    "KH": "🇰🇭",
    "JP": "🇯🇵",
}


def get_bin_info(bin):
    # Hacer una consulta a una API de BIN para obtener la información general del BIN
    url = f"https://lookup.binlist.net/{bin}"
    response = requests.get(url)
    if response.status_code == 200:
        bin_info = response.json()
        brand = bin_info.get("brand", "Desconocido")
        country_name = bin_info.get("country", {}).get("name", "Desconocido")
        country_code = bin_info.get("country", {}).get("alpha2", None)
        bank = bin_info.get("bank", {}).get("name", "Desconocido")
        if country_code in COUNTRY_FLAGS:
            country_flag = COUNTRY_FLAGS[country_code]
            return f" ➻ 𝗕𝗿𝗮𝗻𝗱: {brand}\n ➻ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} [ {country_flag} ]\n ➻ 𝗕𝗮𝗻𝗸: {bank}"
        else:
            return f" ➻ 𝗕𝗿𝗮𝗻𝗱: {brand}\n ➻ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_code}\n ➻ 𝗕𝗮𝗻𝗸: {bank}"
    else:
        return "Información del BIN no disponible.", None


#######################################################################################################################
#######################################################################################################################

    




































# Manejador para inline query
def inline_query(update, context):
    query = update.inline_query.query
    results = []

    # Genera una respuesta para la inline query
    results.append(
        InlineQueryResultArticle(
            id='1',
            title='Ejemplo de Bot de Telegram',
            input_message_content=InputTextMessageContent(query)
        )
    )
    # Envía los resultados de la inline query
    update.inline_query.answer(results)


# Función de manejo de los botones callback_data
def button_callback(update, context):
    query: CallbackQuery = update.callback_query
    data = query.data  # Obtén el callback_data del botón presionado
    
    # Maneja el callback_data y realiza las acciones correspondientes
    if data == 'fin':
        query.edit_message_caption(caption= "Enjoy! 😄")
        # Programar tarea para eliminar la respuesta del botón después de 3 segundos
        t = Timer(2.0, delete_message, args=(query.message,))
        t.start()
    elif data == 'boton1':
        query.edit_message_caption(caption= "No hay chk, por lo tanto, se paciente.\n⚠️ Mantenimiento: 15-04-2023", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='owner', url='https://t.me/hackerismyname'), InlineKeyboardButton(text='tools', callback_data='tools'), InlineKeyboardButton(text='finalizar 🍎', callback_data='fin')]]))
    elif data == 'tools':
        query.edit_message_caption(caption= """
𝗧𝗼𝗼𝗹𝘀 ↆ
        
[🍎] 𝗖𝗢𝗠𝗔𝗡𝗗𝗢: /bin
𝗙𝗼𝗿𝗺𝗮𝘁:  <code>/bin 411204</code>
State: ✅

[🍎] 𝗖𝗢𝗠𝗔𝗡𝗗𝗢: /mail
𝗙𝗼𝗿𝗺𝗮𝘁:  <code>/mail</code>
State: ✅

[🍎] 𝗖𝗢𝗠𝗔𝗡𝗗𝗢: /gen
𝗙𝗼𝗿𝗺𝗮𝘁:  <code>/gen 411204</code>
State: ⚠️

[🍎] 𝗖𝗢𝗠𝗔𝗡𝗗𝗢: /sk
𝗙𝗼𝗿𝗺𝗮𝘁:  <code>/sk sk_live</code>
State: ❌

[🍎] 𝗖𝗢𝗠𝗔𝗡𝗗𝗢: /tr
𝗙𝗼𝗿𝗺𝗮𝘁:  <code>/tr text</code>
State: ❌""", parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='← volver', callback_data='return1'),InlineKeyboardButton(text='finalizar 🍎', callback_data='fin') ]]))
        
    elif data == 'return1':
        query.edit_message_caption(caption= "No hay chk, por lo tanto, se paciente.\n⚠️ Mantenimiento: 15-04-2023", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='owner', url='https://t.me/hackerismyname'), InlineKeyboardButton(text='tools', callback_data='tools'), InlineKeyboardButton(text='finalizar 🍎', callback_data='fin')]]))

    if data == 'fin2':
        query.edit_message_text(text= "Enjoy! 😄")
        # Programar tarea para eliminar la respuesta del botón después de 3 segundos
        t = Timer(2.0, delete_message, args=(query.message,))
        t.start()


# Definir función para eliminar mensaje
def delete_message(message):
    message.delete()

def main():
    # Crea el Updater con el token del bot y use_context=True
    updater = Updater(TOKEN)

    # Obtén el Dispatcher para registrar los manejadores
    dispatcher = updater.dispatcher

    # Registra el manejador para inline query
    dispatcher.add_handler(InlineQueryHandler(inline_query))

#_____________________________________________________________________________________________________
    dispatcher.add_handler(CommandHandler("start", start_command))
    updater.dispatcher.add_handler(CommandHandler("bin", bin_command))
    dispatcher.add_handler(CommandHandler("key", key_command))
    dispatcher.add_handler(CommandHandler("genkey", key_command1))
    dispatcher.add_handler(CommandHandler("my", my_command))
    dispatcher.add_handler(CommandHandler('mail', generar_correo_temporal))
    dispatcher.add_handler(CommandHandler("gen", generate_cards))
    # Agregar el manejador del comando /claim
    claim_handler = CommandHandler('claim', claim_key)
    dispatcher.add_handler(claim_handler)
    dispatcher.add_handler(CommandHandler("userlist", userlist))
    dispatcher.add_handler(CommandHandler("register", register))
#_____________________________________________________________________________________________________
    updater.dispatcher.add_handler(CallbackQueryHandler(button_callback))















    # Inicia el bot
    updater.start_polling()
    logging.info('Bot de Telegram iniciado')
    updater.idle()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f'Error en la ejecución del bot: {e}')

