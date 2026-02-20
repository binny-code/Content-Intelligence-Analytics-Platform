import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_content(text):
    prompt = f"""
    Analyze the following content.
    1. Extract keywords
    2. Suggest category
    3. Summarize in 2 lines

    Content: {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    return response['choices'][0]['message']['content']
