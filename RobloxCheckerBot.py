# Импорт
import requests
import telebot
# Создать бота
bot = telebot.TeleBot("5991042188:AAGRfAZfr_33YtcOJQPtkt9wC6SZ8iUtXF8")
# При старте
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🕹 Добро Пожаловать в Roblox Checker!\n📛Здесь ты проверяешь работает ли какие-то друзья и т. д.\n⌨️Введи команду /help, чтобы узнать все команды")
# Помощь
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "❓Список команд:\n/abtesting\n/accountinformation\n/accountsettings\n/adconfiguration\n/ads\n/api\n/assetdelivery\n/auth\n/avatar\n/badges\n/billing\n/catalog\n/chat\n/clientsettings\n/clientsettingscdn\n/clienttelemetry\n/contentstore\n/contacts\n/develop\n/economy\n/economycreatorstats\n/engagementpayouts\n/ephemeralcounters\n/followings\n/friends\n/gameinternationalization\n/gamejoin\n/gamepersistence\n/games\n/groups\n/groupsmoderation\n/invertory\n/itemconfiguration\n/lms\n/locale\n/localizationtables\n/metrics\n/notifications\n/points\n/premiumfeatures\n/presence\n/privatemessages\n/publish\n/realtime\n/share\n/search\n/textfilter\n/thumbnails\n/thumbnailsresizer\n/trades\n/translationroles\n/translations\n/twostepverification\n/usermoderation\n/users\n/voice")
# Чекает ссылку
@bot.message_handler(commands=['abtesting'])
def abtesting(message):
    url = requests.get("https://abtesting.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['accountinformation'])
def accountinformation(message):
    url = requests.get("https://accountinformation.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['accountsettings'])
def accountsettings(message):
    url = requests.get("https://accountsettings.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['adconfiguration'])
def adconfiguration(message):
    url = requests.get("https://adconfiguration.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['ads'])
def ads(message):
    url = requests.get("https://ads.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['api'])
def api(message):
    url = requests.get("https://api.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['assetdelivery'])
def assetdelivery(message):
    url = requests.get("https://assetdelivery.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['auth'])
def auth(message):
    url = requests.get("https://auth.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['avatar'])
def avatar(message):
    url = requests.get("https://avatar.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['badges'])
def badges(message):
    url = requests.get("https://badges.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['billing'])
def billing(message):
    url = requests.get("https://billing.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['catalog'])
def catalog(message):
    url = requests.get("https://catalog.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['chat'])
def chat(message):
    url = requests.get("https://chat.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['clientsettings'])
def clintsettings(message):
    url = requests.get("https://clientsettings.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['clientsettingscdn'])
def clientsettingscdn(message):
    url = requests.get("https://clientsettingscdn.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['client-telemetry'])
def clienttelemetry(message):
    url = requests.get("https://client-telemetry.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['contentstore'])
def contentstore(message):
    url = requests.get("https://contentstore.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['contacts'])
def contacts(message):
    url = requests.get("https://contacts.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['develop'])
def develop(message):
    url = requests.get("https://develop.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['economy'])
def economy(message):
    url = requests.get("https://economy.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['economycreatorstats'])
def economycreatorstats(message):
    url = requests.get("https://economycreatorstats.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['engagementpayouts'])
def engagementpayouts(message):
    url = requests.get("https://engagementpayouts.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['ephemeralcounters'])
def ephemeralcounters(message):
    url = requests.get("https://ephemeralcounters.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['followings'])
def followings(message):
    url = requests.get("https://followings.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['friends'])
def friends(message):
    url = requests.get("https://friends.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['gameinternationalization'])
def gameinternationalization(message):
    url = requests.get("https://gameinternationalization.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['gamejoin'])
def gamejoin(message):
    url = requests.get("https://gamejoin.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['gamepersistence'])
def gamepersistence(message):
    url = requests.get("https://gamepersistence.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['games'])
def games(message):
    url = requests.get("https://games.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['groups'])
def groups(message):
    url = requests.get("https://groups.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['groupsmoderation'])
def groupmoderation(message):
    url = requests.get("https://groupmoderation.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['invertory'])
def invertory(message):
    url = requests.get("https://invertory.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['itemconfiguration'])
def itemconfiguration(message):
    url = requests.get("https://itemconfiguration.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['lms'])
def lms(message):
    url = requests.get("https://lms.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['locale'])
def locale(message):
    url = requests.get("https://locale.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['localizationtables'])
def localizationtables(message):
    url = requests.get("https://localizationtables.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['metrics'])
def metrics(message):
    url = requests.get("https://metrics.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['notifications'])
def notifications(message):
    url = requests.get("https://notifications.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['points'])
def points(message):
    url = requests.get("https://points.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['premiumfeatures'])
def premiumfeatures(message):
    url = requests.get("https://premiumfeatures.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['presence'])
def presence(message):
    url = requests.get("https://presence.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['privatemessages'])
def premiumfeatures(message):
    url = requests.get("https://privatemessages.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['publish'])
def publish(message):
    url = requests.get("https://publish.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['realtime'])
def realtime(message):
    url = requests.get("https://realtime.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['share'])
def share(message):
    url = requests.get("https://share.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['search'])
def search(message):
    url = requests.get("https://search.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['textfilter'])
def textfilter(message):
    url = requests.get("https://textfilter.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['thumbnails'])
def thumbnails(message):
    url = requests.get("https://thumbnails.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['thumbnailsresizer'])
def thumbnailsresizer(message):
    url = requests.get("https://thumbnailsresizer.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['trades'])
def trades(message):
    url = requests.get("https://trades.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['translationroles'])
def translationroles(message):
    url = requests.get("https://translationroles.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['translations'])
def translations(message):
    url = requests.get("https://translations.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['twostepverification'])
def twostepverification(message):
    url = requests.get("https://twostepverification.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['usermoderation'])
def usermoderation(message):
    url = requests.get("https://usermoderation.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['users'])
def users(message):
    url = requests.get("https://users.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
# Чекает ссылку
@bot.message_handler(commands=['voice'])
def voice(message):
    url = requests.get("https://voice.roblox.com")
    if url.status_code == 200:
        bot.send_message(message.chat.id, "🌐 Активный!")
    else:
        bot.send_message(message.chat.id, "❌ Неактивный!")
bot.polling()
