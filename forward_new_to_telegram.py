import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import telebot
import config

# Authenticate with VK API
vk_session = vk_api.VkApi(token=config.vk_token)
vk = vk_session.get_api()

# Authenticate with Telegram API
bot = telebot.TeleBot(config.tgbot_token)

# Set the Telegram user ID of the user you want to send messages to
user_id = config.tguser_id

# Create an instance of the VkLongPoll class
longpoll = VkLongPoll(vk_session)


# Define a function to handle incoming messages
def handle_message(event):
    message_id = event.message_id
    message = vk.messages.getById(message_ids=message_id)['items'][0]
    peer_id = vk.messages.getById(message_ids=message_id)['items'][0]['peer_id']
    from_id = vk.messages.getById(message_ids=message_id)['items'][0]['from_id']
    contentCase = vk.messages.getById(message_ids=message_id)['items'][0]['attachments']
    if contentCase:
        for i in contentCase:
            if i['type'] == 'audio':
                audioName = i['audio']['title']
                audioArtist = i['audio']['artist']
                audioCoverArt = i['audio']['album']['thumb']['photo_1200']
                audioURL = i['audio']['url']
                bot.send_message(
                    chat_id=user_id,
                    text='message:' +
                         '\n <b>peer_id:</b> ' + str(peer_id) +
                         '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                         '\n <b>type:</b> audio' +
                         '\n <b>content:</b> ' +
                         '\n  <b>name:</b> ' + audioName +
                         '\n  <b>artist:</b> ' + audioArtist +
                         '\n  <b>cover art:</b> <a href="' + audioCoverArt + '">link</a>' +
                         '\n  <b>url:</b> <a href="' + audioURL + '">link</a>',
                    parse_mode="HTML")
            elif i['type'] == 'video':
                videoURL = i['video']['player']
                videoTitle = i['video']['title']
                bot.send_message(
                    chat_id=user_id,
                    text='message:' +
                         '\n <b>peer_id:</b> ' + str(peer_id) +
                         '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                         '\n <b>type:</b> video' +
                         '\n <b>content:</b> ' +
                         '\n  <b>title:</b> ' + videoTitle +
                         '\n  <b>URL:</b> <a href="' + videoURL + '">link</a>',
                    parse_mode="HTML")
            elif i['type'] == 'photo':
                photoDescription = i['photo']['text']
                photoMaxSizeUrl = i['photo']['sizes'][len(i['photo']['sizes']) - 1]['url']
                bot.send_message(
                    chat_id=user_id,
                    text='message:' +
                         '\n <b>peer_id:</b> ' + str(peer_id) +
                         '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                         '\n <b>type:</b> photo' +
                         '\n <b>content:</b> ' +
                         '\n  <b>description:</b> ' + photoDescription +
                         '\n  <b>url:</b> <a href="' + photoMaxSizeUrl + '">link</a>',
                    parse_mode="HTML")
    else:
        bot.send_message(
            chat_id=user_id,
            text='message:' +
                 '\n <b>peer_id:</b> ' + str(peer_id) +
                 '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                 '\n <b>content:</b> ' + str(message),
            parse_mode="HTML")


# Define a function to handle outgoing messages updated
def handle_edit(event):
    message_id = event.message_id
    message = vk.messages.getById(message_ids=message_id)['items'][0]
    peer_id = vk.messages.getById(message_ids=message_id)['items'][0]['peer_id']
    from_id = vk.messages.getById(message_ids=message_id)['items'][0]['from_id']
    contentCase = vk.messages.getById(message_ids=message_id)['items'][0]['attachments']
    if contentCase:
        for i in contentCase:
            if i['type'] == 'audio':
                audioName = i['audio']['title']
                audioArtist = i['audio']['artist']
                audioCoverArt = i['audio']['album']['thumb']['photo_1200']
                audioURL = i['audio']['url']
                bot.send_message(
                    chat_id=user_id,
                    text='message:' +
                         '\n <b>peer_id:</b> ' + str(peer_id) +
                         '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                         '\n <b>outcoming</b>' +
                         '\n <b>type:</b> audio' +
                         '\n <b>content:</b> ' +
                         '\n  <b>name:</b> ' + audioName +
                         '\n  <b>artist:</b> ' + audioArtist +
                         '\n  <b>cover art:</b> <a href="' + audioCoverArt + '">link</a>' +
                         '\n  <b>url:</b> <a href="' + audioURL + '">link</a>',
                    parse_mode="HTML")
            elif i['type'] == 'video':
                videoURL = i['video']['player']
                videoTitle = i['video']['title']
                bot.send_message(
                    chat_id=user_id,
                    text='message:' +
                         '\n <b>peer_id:</b> ' + str(peer_id) +
                         '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                         '\n <b>outcoming</b>' +
                         '\n <b>type:</b> video' +
                         '\n <b>content:</b> ' +
                         '\n  <b>title:</b> ' + videoTitle +
                         '\n  <b>URL:</b> <a href="' + videoURL + '">link</a>',
                    parse_mode="HTML")
            elif i['type'] == 'photo':
                photoDescription = i['photo']['text']
                photoMaxSizeUrl = i['photo']['sizes'][len(i['photo']['sizes']) - 1]['url']
                bot.send_message(
                    chat_id=user_id,
                    text='message:' +
                         '\n <b>peer_id:</b> ' + str(peer_id) +
                         '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                         '\n <b>outcoming</b>' +
                         '\n <b>type:</b> photo' +
                         '\n <b>content:</b> ' +
                         '\n  <b>description:</b> ' + photoDescription +
                         '\n  <b>url:</b> <a href="' + photoMaxSizeUrl + '">link</a>',
                    parse_mode="HTML")
    else:
        bot.send_message(
            chat_id=user_id,
            text='message:' +
                 '\n <b>peer_id:</b> ' + str(peer_id) +
                 '\n <b>sender:</b> <a href="https://vk.com/id' + str(from_id) + '">link</a>' +
                 '\n <b>outcoming</b>' +
                 '\n <b>content:</b> ' + str(message),
            parse_mode="HTML")


# Listen for incoming and outgoing messages
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        handle_message(event)
    elif event.type == VkEventType.MESSAGE_NEW and event.from_me:
        handle_edit(event)
