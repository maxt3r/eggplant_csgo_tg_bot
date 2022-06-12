A Telegram bot I made for a private group that starts our own CS:GO server when needed. Comands:

    /start
    /status
    /help

# Setup

Install requirements:
`pip install -r requirements.txt`

Create the `keys.py` file with all the settings and API keys:

    BotToken = "..."
    AwsRegion = "..."
    ServerInstanceID = "..."
    AwsKey = "..."
    AwsSecret = "..."

Unfortunately it relies on an npm package to display the server info. It needs to be globally installed:

    npm install gamedig -g

# Run

    python3 main.py
