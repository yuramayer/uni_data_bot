# Ботик ChatGPT + Yandex S3

<p align="right">
  <a href="README.md">Read on English</a>
</p>

![Bot Picture](img/bot_pic.png)

Учебный проект по курсу "Инжиниринг данных"

## Стек

- Бот на Aiogram ✈️
- Генерация ответа на GPT-4o 🤖
- Data lake на Yandex S3 ☁️
- Обработка через Yandex Query ⚙️
- Дашборд на Yandex DataLens 🌻

### Почему такой стек?

Я выбрал aiogram и OpenAI API потому что раньше работал с ними,
и всё было классно) Я думал между Postgres и S3, и остановился
на S3 из-за удобной яндексовской экосистемы S3-Query-DataLens

## Результат

Бота можно потыкать здесь:
**[t.me/botrqst_gpt_bot](https://t.me/botrqst_gpt_bot)**

Ссылку на дашборд я прикрепил к домашнему заданию. К дашборду я добавил
табличку, в которой можно интерактивно почитать логи

## Собственный деплой

Чтобы развернуть бота, создай и заполни в директории `.env`-файл такого формата:

```env
BOT_TOKEN=''
ADMINS=''
OPENAI_API_KEY=''
CLOUD_S3_ID_KEY=''
CLOUD_S3_SECRET_KEY=''
BUCKET_NAME=''
```

> ⚠️ OpenAI API не доступен в России,
поэтому деплоить нужно на зарубежном VPS 😢
