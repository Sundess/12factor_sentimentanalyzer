"""
Analyzes the text sentiment
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def sentiment_analyzer(text):
    """
    Take text as input and analyzer the text.
    Categories it into Positive, Negative or Neutral & returns it.
    """

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a sentiment analyzer expert, "
                "analyze the sentiment of the text "
                "as give the sentiment back. "
                "It should be one word answer "
                "either positive, negative or neutral",
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    print(completion.choices[0].message.content)
    result = completion.choices[0].message.content

    return result
