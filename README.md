A Telegram bot I made for a private group that starts our own CS:GO server when needed. Comands:

    /start
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

# Run

    python3 main.py
