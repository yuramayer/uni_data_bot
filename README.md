# ChatGPT Bot + Yandex S3

<p align="right">
  <a href="README_ru.md">Читать на русском</a>
</p>

![Bot Picture](img/bot_pic.png)

A small educational project from the “Data Engineering” course.

## Stack

- Aiogram Telegram bot ✈️  
- GPT-4o response generation 🤖  
- Data lake on Yandex S3 ☁️  
- Querying with Yandex Query ⚙️  
- Dashboard built in Yandex DataLens 🌻  

### Why this stack?

I chose Aiogram and OpenAI API because I worked with them before,  
and they were easy and fun to use.  
I was choosing between Postgres and S3.  
I picked S3 because it works well with Yandex services  
like Query and DataLens.

## Result

You can try the bot here: 
**[t.me/botrqst_gpt_bot](https://t.me/botrqst_gpt_bot)**

The dashboard link is attached to the homework.  
The dashboard includes a table where you can explore the logs.

## Run it yourself

To run this bot, create a `.env` file in the project folder with this format:

```env
BOT_TOKEN=''
ADMINS=''
OPENAI_API_KEY=''
CLOUD_S3_ID_KEY=''
CLOUD_S3_SECRET_KEY=''
BUCKET_NAME=''
```

> ⚠️ OpenAI API does not work in Russia,
so you’ll need to deploy it on a server outside the country 😢
