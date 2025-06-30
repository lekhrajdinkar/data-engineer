from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
os.environ["OPENAI_API_KEY"] = api_key # set for langchain

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {
            "role": "user",
            "content": "write a haiku about ai"
         }
    ]
)

print(completion.choices[0].message)
