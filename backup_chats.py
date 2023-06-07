# Import requirements and checking its existence
try:
    import vk_api, config
except:
    print('some of required modules not found. run "pip install -r requirements.txt"')


# Simple debug helper
def debug(a):
	if config.debug:
		print(str(a))


# Set up API things
vk_session = vk_api.VkApi(token=config.vk_token)
debug('vk_session set')
vk = vk_session.get_api()
debug('vk set')


# Conversations fetcher
def getChats():
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
									f.write(str('\nmessage:' +
												'\n sender: https://vk.com/id' + str(from_id) +
												'\n type: audio' +
												'\n content: ' +
												'\n  name: ' + audioName +
												'\n  artist: ' + audioArtist +
												'\n  url: ' + audioURL))
								elif i['type'] == 'video':
									videoTitle = i['video']['title']
									try:
										videoURL = i['video']['player']
									except:
										videoURL = 'Unreachable video'
									f.write(str('\nmessage:' +
												'\n sender: https://vk.com/id' + str(from_id) +
												'\n type: video' +
												'\n content: ' +
												'\n  title: ' + videoTitle +
												'\n  url: ' + videoURL))
								elif i['type'] == 'photo':
									photoDescription = i['photo']['text']
									photoMaxSizeUrl = i['photo']['sizes'][len(i['photo']['sizes']) - 1]['url']
									f.write(str('\nmessage:' +
												'\n sender: https://vk.com/id' + str(from_id) +
												'\n type: photo' +
												'\n content: ' +
												'\n  description: ' + photoDescription +
												'\n  url: ' + photoMaxSizeUrl))
								debug("media written")
								residcounter = False
						else:
							f.write(str('\nmessage:' +
										'\n sender: https://vk.com/id' + str(from_id) +
										'\n type: text' +
										'\n content: ' + str(i['text'])))
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


# Photos fetcher
def getPhotos():
	photos = vk.photos.getAll()
	countOfPhotos = photos['count']
	offset = 0
	while offset<countOfPhotos:
		photos = vk.photos.getAll(count=200, offset=offset)
		offset+=200
		debug('Fetching ' + str(countOfPhotos) +' photos')
		filename = f"data/photos.txt"
		with open(filename, 'w', encoding='utf-8') as f:
			for i in photos['items']:
				f.write('text: ' + i['text'] + '\n')
				sizes = sorted(i['sizes'], key=lambda d: d['type'], reverse=True)
				f.write('url: ' + sizes[0]['url'] + '\n\n')
				debug('Type of photo size: ' + sizes[0]['type'])


# Run selected things
if config.chats:
	getChats()
if config.photos:
	getPhotos()
