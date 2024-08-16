from openai import OpenAI

import pytesseract
from PIL import Image

import os


client = OpenAI(
    api_key=os.getenv('AI_API_KEY'),
)

def get_message():
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a financial assistant who manages incomes and expenses by reading receipts from stores."},
                {
                    "role": "user",
                    "content": "Привет, я хочу чтобы ты рассчитал мои расходы за сегодня, вот ссылка на мой чек: https://i.imgur.com/lafyabB.jpeg"
                }
            ]
        )

        return True, chat_completion.choices[0].message.content
    except Exception as E:
        return False, E


print(get_message())