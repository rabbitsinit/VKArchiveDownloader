import vk_api

logs = True

def debug(a):
	if logs:
		print(str(a))

# Replace with your token from https://vkhost.github.io/
TOKEN = 'VK USER TOKEN'

# Log in using the token
vk_session = vk_api.VkApi(token=TOKEN)
debug('vk_session set')

# Get the API object
vk = vk_session.get_api()
debug('vk set')

# Get all conversations for the user
amountOfConversations = vk.messages.getConversations(count=200)['count']
conversationsRemaining = amountOfConversations
debug("amountOfConversations: " + str(amountOfConversations))
debug("conversationsRemaining: " + str(conversationsRemaining))

while conversationsRemaining > 0:
	debug("conversationsRemaining is more than 0, cycle started")
	conversations = vk.messages.getConversations(count=200, offset=amountOfConversations-conversationsRemaining)['items']
	conversationsRemaining -= 200
	debug("got conversations")
	debug(str(conversations))
	debug("conversationsRemaining: " + str(conversationsRemaining))
	# Loop through each conversation and download the history to a file
	for conversation in conversations:
		debug("conversation cycle started")
		residcounter = False
		# Get the conversation ID and title/name
		conversation_id = conversation['conversation']['peer']['id']
		conversation_title = conversation['conversation']['chat_settings']['title'] if 'chat_settings' in conversation['conversation'] else None
		filename = f"data/chats/{conversation_id}.txt"
		dialog_len = conversation['conversation']['last_message_id']
		friend_history = []
		debug("vars set")

		with open(filename, 'w', encoding='utf-8') as f:
			debug("file " + filename + " opened")
			f.write('conversation: ' + '\n  title: ' + str(conversation_title) + '\n  id: ' + str(conversation_id) + '\n\n')
			resid = dialog_len
			offset = 0
			while resid > 0:
				historyDump = vk.messages.getHistory(peer_id=conversation_id, count=200, offset=offset)['items']
				for i in historyDump:
					contentCase = i['attachments']
					from_id = i['from_id']
					if contentCase:
						for i in contentCase:
							if i['type'] == 'audio':
								audioName = i['audio']['title']
								audioArtist = i['audio']['artist']
								audioURL = i['audio']['url']
								f.write(str('\nsender: https://vk.com/id' + str(from_id) +
										 '\n  type: audio' +
										 '\n  content: ' +
										 '\n    name: ' + audioName +
										 '\n    artist: ' + audioArtist +
										 '\n    url: ' + audioURL + '\n'))
							elif i['type'] == 'video':
								videoTitle = i['video']['title']
								try:
									videoURL = i['video']['player']
								except:
									videoURL = 'Unreachable video'
								f.write(str('\nsender: https://vk.com/id' + str(from_id) +
										    '\n  type: video' +
										    '\n  content: ' +
										    '\n    title: ' + videoTitle +
										    '\n    url: ' + videoURL))
							elif i['type'] == 'photo':
								photoDescription = i['photo']['text']
								photoSizes = i['photo']['sizes']
								photoUrl = i['photo']['sizes'][len(photoSizes) - 1]['url']
								f.write(str('\nsender: https://vk.com/id' + str(from_id) +
											'\n  type: photo' +
											'\n  content: ' +
											'\n    description: ' + photoDescription +
											'\n    url: ' + photoUrl))
							debug("media written")
							residcounter = False
					else:
						f.write(str('\nsender: https://vk.com/id' + str(from_id) +
									'\n  content: ' + str(i['text']) +
									'\n'))
						debug("text written")
						residcounter = False
				if (resid > 0) and (not residcounter):
					debug("reset offset, resid=" + str(resid) + ", offset=" + str(offset) + ", dialog_len=" + str(dialog_len))
					resid -= 200
					offset += 200
					residcounter = True
				else:
					debug("conversation saved")
					break