import vk_api

# Replace with your token
TOKEN = ''

# Log in using the token
vk_session = vk_api.VkApi(token=TOKEN)

# Get the API object
vk = vk_session.get_api()

# Get all conversations for the user
conversations = vk.messages.getConversations(count=200)['items']

# Loop through each conversation and download the history to a file
for conversation in conversations:
	# Get the conversation ID and title/name
	conversation_id = conversation['conversation']['peer']['id']
	conversation_title = conversation['conversation']['chat_settings']['title'] if 'chat_settings' in conversation[
		'conversation'] else None
	filename = f"{conversation_id}.txt"

	# Get the conversation history
	history = vk.messages.getHistory(peer_id=conversation_id, count=200)['items']

	# Write the history to a file
	with open(filename, 'w', encoding='utf-8') as f:
		f.write(str(conversation_title) + "\n")
		for message in history:
			if 'text' in message:
				f.write(str(message['from_id']) + ': ' + message['text'] + '\n')