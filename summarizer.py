import os
import openai

#config
OPENAI_API_KEY = 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


openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    prompt = (
        "Summarize in 2-3 sentences about the content on the website and focus on updates about the SAT, AP exams, or other major announcements:"
        + text[:2000] # <- truncate to fit the token limits
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
