import dotenv 
import os 
import openai # Importando a lib da openAI

dotenv.load_dotenv()
openai.api_key = os.getenv("KEY") # Informando nossa chave de acesso


prompt = "Qual maior time de Minas Gerais?"
prompt2 = "Qual seu nome?" 

response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt2,
    temperature=0.7,
    max_tokens= 2048,
    n=1, 
    stop=None 
)['choices'][0]['text'].strip()

print(response)