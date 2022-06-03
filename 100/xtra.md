### 1.
```sh
pip install telethon
# More info - https://docs.telethon.dev/en/latest/

# Get 'api_id' and 'api_hash' :
https://my.telegram.org/

# the API development tools :
https://my.telegram.org/apps

# Get your API credentials :
https://core.telegram.org/api/obtaining_api_id
```

### 2.
```py
import configparser # to read API credentials from config files
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
```

### 3.
```
[Telegram]
# no need for quotes

# you can get telegram development credentials in API Dev Tools
api_id = Telegram-API-ID
api_hash = Telegram-API-Hash

# use full phone number including + and country code
phone = Your-Telegram-Phone-Number
username = Your-Telegram-Username
```
