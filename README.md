# MyBot

This is my first Discord Bot Project in GitHub. Usage of this is own Methods of learning and improvement!

## Setup

1. Create Discord devolper app: [Link](https://discord.com/developers/applications/)
1. Activate  Discord (developer) -> Bot -> 'MESSAGE CONTENT INTENT'.
1. Create .env and enter your token from Discord (developer) -> Bot
1. Discord (developer) -> OAuth2 -> URL Generator.
    ~~~
    SCOPES: 'bot'
    BOT PERMISSIONS: 'Send Messages'
    ~~~
   -> copy GENERATED URL  
   -> paste into browser  
   -> select server

1. Create and activate virtual environment (optional)
    ~~~
   cd src
   python3 -m venv venv
   source venv/bin/activate
    ~~~

1. Install dependencies
    ~~~
    pip3 install -r requirements.txt
    ~~~

1. Execute main
    ~~~
    python3 main.py
