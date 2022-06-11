# Setup

Install requirements:
`pip install -r requirements.txt`

Create the `keys.py` file with all the settings and API keys:

    BotToken = "..."
    AwsRegion = "..."
    ServerInstanceID = "..."
    AwsKey = "..."
    AwsSecret = "..."

Configure AWS CLI with your credentials:

    aws configure

# Run

      python3 main.py
