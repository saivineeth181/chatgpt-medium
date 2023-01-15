import openai
import json
openai.api_key = "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"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()
