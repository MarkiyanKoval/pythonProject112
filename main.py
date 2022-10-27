
import telebot, wikipedia, re

bot = telebot.TeleBot('5719094069:AAEOGcooEQMhzQnIs4fCSzaiNwO95zxKkww')

wikipedia.set_lang("en")

def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext=ny.content[:1000]

        wikimas=wikitext.split('.')

        wikimas = wikimas[:-1]

        wikitext2 = ''

        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break

        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'The encyclopedia has no information about it'

@bot.message_handler(commands=["info"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'send me the country and I will find information about it')
import sqlite3
from telebot import TeleBot
conn = sqlite3.connect("data/WWWWWWWWWWWWWWWW.db", check_same_thread=False)

cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Hello how are you? I am bot geograph.For more /menu ")

@bot.message_handler(commands=["menu"])
def start_message(message):
    bot.send_message(message.chat.id,'/capital - capital cities,  '
                                     '/area - to get area,  '
                                     '/list - to get list of all europe countries')

@bot.message_handler(commands=["menu"])
def start_message(message):
    bot.send_message(message.chat.id,'')

@bot.message_handler(commands=["area "])
def start_message(message):
    bot.send_message(message.chat.id, '')



@bot.message_handler(commands=["list "])
def start_message(message):
    bot.send_message(message.chat.id, '')

@bot.message_handler(commands=["capital "])
def start_message(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    if message.text.lower() == "europe":
        bot.send_message(message.chat.id,"ok, there are 48 countries, Which country interests you")
    if message.text.lower() == "/area":
        bot.send_message(message.chat.id,'print country to get area')
    if message.text.lower() == "/list":
        bot.send_message(message.chat.id,"andorra liechtenstein armenia  lithuania austria luxembourg azerbaijan malta belarus moldova belgium monaco bosnia herzegovina montenegro bulgaria netherlands croatia norway cyprus  poland czech republic  portugal denmark  romania estonia  russia finland  san marino north macedonia serbia france  slovakia georgia  slovenia germany  spain greece  sweden hungary sweden iceland switzerland ireland turkey italy  ukraine  united kingdom  albania latvia")
    if message.text.lower() == "/capital":
        bot.send_message(message.chat.id,'print country to get capital city')
    if message.text.lower() == "croatia":
        bot.send_message(message.chat.id, "zagreb is the capital ")
    if message.text.lower() == "albania":
        bot.send_message(message.chat.id, "Tirana is the capital")
    if message.text.lower() == "andorra":
        bot.send_message(message.chat.id, " Andorra la Vella is the capital")
    if message.text.lower() == "austria":
        bot.send_message(message.chat.id, " Vienna is the capital")
    if message.text.lower() == "belarus":
        bot.send_message(message.chat.id, " Minsk is the capital")
    if message.text.lower() == "belgium":
        bot.send_message(message.chat.id, "  Brussels  the capital")
    if message.text.lower() == "bosnia and herzegovina":
        bot.send_message(message.chat.id, " Sarajevo is the capital")
    if message.text.lower() == "bulgaria":
        bot.send_message(message.chat.id, " Sofia is the capital")
    if message.text.lower() == "czechia":
        bot.send_message(message.chat.id, " Prague is the capital")
    if message.text.lower() == "denmark":
        bot.send_message(message.chat.id, " Copenhagen is the capital")
    if message.text.lower() == "estonia":
        bot.send_message(message.chat.id, " Tallinn is the capital")
    if message.text.lower() == "finland":
        bot.send_message(message.chat.id, " Helsinki is the capital")
    if message.text.lower() == "france":
        bot.send_message(message.chat.id, " Paris is the capital")
    if message.text.lower() == "germany":
        bot.send_message(message.chat.id, " Berlin is the capital")
    if message.text.lower() == "greece":
        bot.send_message(message.chat.id, " Athens is the capital")
    if message.text.lower() == "hungary":
        bot.send_message(message.chat.id, " Budapest is the capital")
    if message.text.lower() == "iceland":
        bot.send_message(message.chat.id, " Reykjavik is the capital")
    if message.text.lower() == "ireland":
        bot.send_message(message.chat.id, " Dublin is the capital")
    if message.text.lower() == "italy":
        bot.send_message(message.chat.id, " Rome is the capital")
    if message.text.lower() == "latvia":
        bot.send_message(message.chat.id, " Riga is the capital")
    if message.text.lower() == "liechtenstein":
        bot.send_message(message.chat.id, " Vaduz is the capital")
    if message.text.lower() == "lithuania":
        bot.send_message(message.chat.id, " Vilnius is the capital")
    if message.text.lower() == "luxembourg":
        bot.send_message(message.chat.id, " Luxembourg is the capital")
    if message.text.lower() == "malta":
        bot.send_message(message.chat.id, " Valletta is the capital")
    if message.text.lower() == "moldova":
        bot.send_message(message.chat.id, " Chisinau is the capital")
    if message.text.lower() == "monaco":
        bot.send_message(message.chat.id, " Monaco is the capital")
    if message.text.lower() == "montenegro":
        bot.send_message(message.chat.id, " Podgorica is the capital")
    if message.text.lower() == "netherlands":
        bot.send_message(message.chat.id, " Amsterdam is the capital")
    if message.text.lower() == "north macedonia":
        bot.send_message(message.chat.id, " Skopje is the capital")
    if message.text.lower() == "norway":
        bot.send_message(message.chat.id, " Oslo is the capital")
    if message.text.lower() == "poland":
        bot.send_message(message.chat.id, " Warsaw is the capital")
    if message.text.lower() == "portugal":
        bot.send_message(message.chat.id, " Lisbon is the capital")
    if message.text.lower() == "romania":
        bot.send_message(message.chat.id, " Bucharest is the capital")
    if message.text.lower() == "russia":
        bot.send_message(message.chat.id, " Moscow is the capital")
    if message.text.lower() == "san marino":
        bot.send_message(message.chat.id, " San Marino is the capital")
    if message.text.lower() == "serbia":
        bot.send_message(message.chat.id, "  Belgrade is the capital")
    if message.text.lower() == "slovakia":
        bot.send_message(message.chat.id, " Bratislava is the capital")
    if message.text.lower() == "slovenia":
        bot.send_message(message.chat.id, " Ljubljana is the capital")
    if message.text.lower() == "spain":
        bot.send_message(message.chat.id, " Madrid is the capital")
    if message.text.lower() == "sweden":
        bot.send_message(message.chat.id, "  Stockholm is the capital")
    if message.text.lower() == "switzerland":
        bot.send_message(message.chat.id, "  Bern is the capital")
    if message.text.lower() == "ukraine":
        bot.send_message(message.chat.id, " Kiev is the capital")
    if message.text.lower() == "united Kingdom":
        bot.send_message(message.chat.id, " London is the capital")
    if message.text.lower() == "area of croatia":
        bot.send_message(message.chat.id, " 56,594km2")
    if message.text.lower() == "area of albania":
        bot.send_message(message.chat.id, "28,748km2  ")
    if message.text.lower() == "area of andorra":
        bot.send_message(message.chat.id, " 468km2  ")
    if message.text.lower() == "area of austria":
        bot.send_message(message.chat.id, " 83,858km2")
    if message.text.lower() == "area of belarus":
        bot.send_message(message.chat.id, " 207,600km2")
    if message.text.lower() == "area of belgium":
        bot.send_message(message.chat.id, " 30,510km2   ")
    if message.text.lower() == "area of bosnia and herzegovina":
        bot.send_message(message.chat.id, "51,129km2   ")
    if message.text.lower() == "area of bulgaria":
        bot.send_message(message.chat.id, " 110,994km2")
    if message.text.lower() == "area of czechia":
        bot.send_message(message.chat.id, "78,866km2")
    if message.text.lower() == "area of denmark":
        bot.send_message(message.chat.id, "44,493km2 ")
    if message.text.lower() == "area of estonia":
        bot.send_message(message.chat.id, " 45,339km2")
    if message.text.lower() == "area of finland":
        bot.send_message(message.chat.id, "338,145km2 ")
    if message.text.lower() == "area of france":
        bot.send_message(message.chat.id, " 551 595km2")
    if message.text.lower() == "area of germany":
        bot.send_message(message.chat.id, " 357,386km2")
    if message.text.lower() == "area of greece":
        bot.send_message(message.chat.id, "131,940km2 ")
    if message.text.lower() == "area of hungary":
        bot.send_message(message.chat.id, " 93,030km2  ")
    if message.text.lower() == "area of iceland":
        bot.send_message(message.chat.id, " 102,775km2")
    if message.text.lower() == "area of ireland":
        bot.send_message(message.chat.id, " 70,273km2")
    if message.text.lower() == "area of italy":
        bot.send_message(message.chat.id, "301,318km2 ")
    if message.text.lower() == "area of latvia":
        bot.send_message(message.chat.id, " 64,589km2")
    if message.text.lower() == "area of liechtenstein":
        bot.send_message(message.chat.id, " 160km2  ")
    if message.text.lower() == "area of lithuania":
        bot.send_message(message.chat.id, " 65,300km2")
    if message.text.lower() == "area of luxembourg":
        bot.send_message(message.chat.id, "2,586km2   ")
    if message.text.lower() == "area of malta":
        bot.send_message(message.chat.id, " 316km2")
    if message.text.lower() == "area of moldova":
        bot.send_message(message.chat.id, "33,846km2  ")
    if message.text.lower() == "area of monaco":
        bot.send_message(message.chat.id, "2km2   ")
    if message.text.lower() == "area of montenegro":
        bot.send_message(message.chat.id, "13,812km2   ")
    if message.text.lower() == "area of netherlands":
        bot.send_message(message.chat.id, " 41,198km2  ")
    if message.text.lower() == "area of north macedonia":
        bot.send_message(message.chat.id, " 25,713km2  ")
    if message.text.lower() == "area of norway":
        bot.send_message(message.chat.id, " 385,178km2")
    if message.text.lower() == "area of poland":
        bot.send_message(message.chat.id, " 312,685km2")
    if message.text.lower() == "area of portugal":
        bot.send_message(message.chat.id, " 88,416km2")
    if message.text.lower() == "area of romania":
        bot.send_message(message.chat.id, "238,397km2 ")
    if message.text.lower() == "area of russia":
        bot.send_message(message.chat.id, "3 756 588 км2")
    if message.text.lower() == "area of san marino":
        bot.send_message(message.chat.id, " 61km2  ")
    if message.text.lower() == "area of serbia":
        bot.send_message(message.chat.id, " 88,361km2")
    if message.text.lower() == "area of slovakia":
        bot.send_message(message.chat.id, " 49,036km2")
    if message.text.lower() == "area of slovenia":
        bot.send_message(message.chat.id, "20,273 km2")
    if message.text.lower() == "area of spain":
        bot.send_message(message.chat.id, "505 992km2 ")
    if message.text.lower() == "area of sweden":
        bot.send_message(message.chat.id, " 450,295km2 ")
    if message.text.lower() == "area of switzerland":
        bot.send_message(message.chat.id, " 41,290km2   ")
    if message.text.lower() == "area of ukraine":
        bot.send_message(message.chat.id, "603 628km2")
    if message.text.lower() == "area of united Kingdom":
        bot.send_message(message.chat.id, " 242,495km2")




    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)




while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)