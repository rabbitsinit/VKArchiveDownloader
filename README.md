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
### 2. Get the access tokens and other important data
Get VK User token [here](https://vkhost.github.io/)

Get Telegram bot token from [BotFather](https://telegram.me/BotFather)

Get Telegram user id [here](https://t.me/userinfobot)
### 3. Configure config.py
Insert your tokens and change variables values if you need
### 4. Create the /data/chats/ in the project folder
