
# Google Sheets Telegram Bot

A Telegram bot for easy management of Google Sheets is my freelance project, which enables administrators to record their income and expenses.


![Logo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdocs.eazybi.com%2Feazybi%2Ffiles%2F2392630%2F43516111%2F1%2F1534792181000%2Fsheets.png&f=1&nofb=1&ipt=2cb39562b8f28440597b7433aead03dd8587723860752b332ae94a0453847df1&ipo=images)


## Deployment

To run this Telegram bot on your machine or server, you need to obtain the credentials.json file from console.cloud.google.com.

1. Create a project.
2. Add the Google Sheets and Google Drive extensions.
3. In the left sidebar, select APIs & Services -> Credentials and create new Credentials (service account).
4. Add this service account as an editor to your Google Sheets document.
5. In the gs_main.py file, specify the name of the sheets file and the worksheet.
Next, create a config.py file with constants TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN.

To run the bot, execute the command:

```bash
  python bot.py
```


## Screenshots
Example of using the bot.

![App Screenshot](https://i.imgur.com/X0Bxxcx.png)

