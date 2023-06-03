import vk_api
import telebot

# Authenticate with VK API
vk_session = vk_api.VkApi(token='vk-token')
vk = vk_session.get_api()

# Authenticate with Telegram API
bot = telebot.TeleBot('bot-token')

# Get the user ID of the user you want to send messages to
user_id = 841914494

# Get a list of conversations that the bot is a member of
conversations = vk.messages.getConversations()

# Loop through each conversation and get the message history
for conversation in conversations['items']:
    conversation_id = conversation['conversation']['peer']['id']
    conversation_type = conversation['conversation']['peer']['type']
    if conversation_type == 'user':
        # If the conversation is with a user, get the message history and send it to the Telegram bot
        history = vk.messages.getHistory(user_id=conversation_id, count=100)
        for message in history['items']:
            if message['from_id'] == vk_session.token['user_id']:
                # If the message is outgoing, send it to the user through the Telegram bot
                message_text = message['text']
                bot.send_message(chat_id=user_id, text=message_text)