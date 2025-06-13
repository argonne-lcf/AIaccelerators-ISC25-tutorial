from openai import OpenAI

client = OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key="f808cb93-7d1d-4d77-82d1-16c3afb3db9d"
)

completion = client.chat.completions.create(
  model="Meta-Llama-3.1-405B-Instruct",
  messages = [
      {"role": "system", "content": "Answer the question in a couple sentences."},
      {"role": "user", "content": "Share a happy story with me"}
    ]
)

print(completion.choices[0].message.content)