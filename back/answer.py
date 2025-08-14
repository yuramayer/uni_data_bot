"""ChatGPT funcs for the bot"""

import openai
from config.conf import OPENAI_API_KEY


client = openai.OpenAI(api_key=OPENAI_API_KEY)


def get_instruction() -> str:
    """Creates instruction for the bot"""
    instruction = """Ты - помощник чат-бота, который должен ответить \
        на любое сообщение пользователя. Пользователь может задать вопрос, \
             написать что-нибудь просто так или просто потролить. Твоя задача \
                - ответить так чтобы пользователю понравилось в зависимости \
                    от того чего хочет пользователь. Дай только ответ"""
    return instruction


def get_question(message) -> str:
    """Get question from the user"""

    question = f"""{message}"""
    return question


def got_problem() -> str:
    """Sends message with the GPT error"""

    txt = """На этапе генерации возникла ошибка 😔\n\n\
        Обратитесь к администратору @botrqst"""
    return txt


def create_answer(message: str):
    """Gets answer from the GPT for the user"""
    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "developer", "content": get_instruction()},
                {
                    "role": "user",
                    "content": get_question(message),
                },
            ],
            model="gpt-4o"
        )
        answer = completion.choices[0].message.content
    except (
        openai.RateLimitError,
        openai.AuthenticationError,
        openai.APIConnectionError,
        openai.APIStatusError,
        openai.OpenAIError
    ):
        return got_problem()

    if answer is None:
        return "Модель не отвечает на ваш запрос 🙁"
    return answer
