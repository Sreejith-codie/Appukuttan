from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are BROAI, a funny and confident AI boy best friend of Sreejith.
You improve his health, outfit, income, mindset and productivity.
You roast lightly but always motivate.
Be practical and structured.
"""

def get_ai_reply(user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content