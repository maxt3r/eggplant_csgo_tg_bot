import json
import logging
import subprocess
import keys
import boto3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# AWS client
awsResource = boto3.resource(
    "ec2",
    region_name=keys.AwsRegion,
    aws_access_key_id=keys.AwsKey,
    aws_secret_access_key=keys.AwsSecret,
)


async def start(update: Update, context):
    if await check_reconnecting(update, context):
        return
    # check if the server is already running
    instance = awsResource.Instance(keys.ServerInstanceID)
    if instance.state["Name"] == "running":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="🙌 Сервер уже включен!"
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="✨ Стартую сервер..."
        )
        instance.start()
        instance.wait_until_running()
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="✅ Сервер работает. Заходите!"
        )


async def help(update: Update, context):
    if await check_reconnecting(update, context):
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Бот умеет включать основной сервер: нужно написать `/start` и все\. Еще можно написать `/status`\. Код [тут](https://github.com/maxt3r/eggplant_csgo_tg_bot) 🍆💦",
        disable_web_page_preview=True,
        parse_mode="MarkdownV2",
    )


async def status(update: Update, context):
    if await check_reconnecting(update, context):
        return

    res = subprocess.run(
        "gamedig --type csgo " + keys.ServerIP, stdout=subprocess.PIPE, shell=True
    ).stdout.decode("utf-8")
    server_info = json.loads(res)

    if "error" in server_info:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="😞 Cервер выключен\. `\start` чтобы включить\.",
            parse_mode = "MarkdownV2"
        )
        return

    map = server_info["map"]
    num_players = server_info["raw"]["numplayers"]
    text = f"🔥 Сервер работает\. Карта `{map}`\. Играют `{num_players}` овощей\."

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=text, parse_mode="MarkdownV2"
    )


async def check_reconnecting(update: Update, context):
    return update.effective_user.username == "milfgard"

if __name__ == "__main__":
    application = ApplicationBuilder().token(keys.BotToken).build()

    start_handler = CommandHandler("start", start)
    status_handler = CommandHandler("status", status)
    help_handler = CommandHandler("help", help)

    application.add_handler(start_handler)
    application.add_handler(status_handler)
    application.add_handler(help_handler)

    application.run_polling()
