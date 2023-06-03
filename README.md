![cover](https://github.com/RabbitsInIT/VKArchiveDownloader/assets/72883689/a8ab9bc0-7f15-4156-a581-1206f690f023)
# VKArchiveDownloader
### Backup chats
This program allows you to download the entire message history in all conversations and with all users in separate files. Each chat is saved in a separate [chat id].txt file
### Forward new to Telegram
This program forwards all new incoming and outgoing messages to Telegram.
## Getting started
### 1. Install the following pip packages:
- **vk_api**
```bash
pip install vk_api
```
- **telebot** (to forward messages in telegram)
```bash
pip install pyTelegramBotAPI
```
### 2. Get the access token VK
You can do this on [this website](https://vkhost.github.io/)
### 3. Get the Telegram bot token
You can get token from [BotFather](https://telegram.me/BotFather)
### 4. Insert your tokens and the id of your Telegram profile into the code 
The identifier of your Telegram profile should consist only of numbers
### 5. Create the /data/chats/ in the project folder
