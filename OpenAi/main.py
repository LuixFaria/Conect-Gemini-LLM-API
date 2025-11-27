from openai import OpenAI
import os

caminho = os.path.join(os.path.dirname(__file__), 'Openai_key.txt')

with open(caminho, 'r') as file:
    api_key=file.read().strip()

client = OpenAI(api_key = api_key)

modelos = client.models.list()

for modelo in modelos.data:
    print(modelo.id)

prompt = 'Que cor é o céu?'

resposta_openAI = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': prompt}
        ],
        temperature=0.2,
        top_p=1.0,
        max_tokens=200,
        stop=['FIM']
)

print(resposta_openAI.choices[0].message.content)