import google.generativeai as genai
import os

#Definindo o caminho que esta a chave (Para fins de teste, deve estar na mesma pasta que o .py)
caminho = os.path.join(os.path.dirname(__file__), 'google_key.txt')

#Lendo a chave do arquivo
with open(caminho, 'r') as arquivo:
    api_key = arquivo.read().strip()

# Configure GenAI
genai.configure(api_key=api_key)

#Lista de modelos disponíveis e sua descrição

modelos = genai.list_models()

for modelo in modelos:
    print(modelo.name + ' (' + modelo.description + ')')

#Modelo teste gemini-1.5-pro (Gratuito)

modelo = genai.GenerativeModel('gemini-2.0-flash')

prompt = 'Como postar esse esse projeto no github?'
#input('Digite um prompt: ')

resposta_modelo = modelo.generate_content(
    prompt,
    generation_config={
        'temperature': 0.1, # Quanto mais perto do 1 mais vasta a resposta porem mais chance de alucinar
        'top_p': 1.0,
        'top_k': 20,
        'max_output_tokens': 500 #Teto de palavras da resposta
    }
)
print(resposta_modelo.text)