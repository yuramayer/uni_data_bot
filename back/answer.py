import openai
from config.conf import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_instruction() -> str:
    instruction = """Ты - помощник чат-бота, который должен ответить \
        на любое сообщение пользователя. Пользователь может задать вопрос, \
             написать что-нибудь просто так или просто потролить. Твоя задача \
                - ответить так чтобы пользователю понравилось в зависимости \
                    от того чего хочет пользователь. Дай только ответ"""
    return instruction


def get_question(message) -> str:
    question = f"""{message}"""
    return question


def got_problem() -> str:
    txt = """На этапе генерации возникла ошибка 😔\n\n\
        Обратитесь к администратору @botrqst"""
    return txt


def create_answer(message: str):
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
    except:
        answer = got_problem()
    if answer is None:
        answer = "Модель не отвечает на ваш запрос 🙁"
    return answer
