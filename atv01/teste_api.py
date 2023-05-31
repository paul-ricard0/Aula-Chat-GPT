
import openai # Importando a lib da openAI

openai.api_key = "KEY" # Informando nossa chave de acesso

prompt = "Qual maior time de Minas Gerais?"

response = openai.Completion.create(
    model="text-davinci-003", # o mecanimos da i.a
    prompt= prompt,
    temperature=0.7, # entre 0 e 2. Valores mais altos como 1,8 tornarão a saída mais aleatória, enquanto valores mais baixos como 0,2 a tornarão mais focada e determinística.
    max_tokens= 100, # Quantidade de retorno (Tokens, padrao 16)
    n=1, # Quantos respostas vão ser geradas
    stop=None # String ou array(4), com palavras de parada caso ele retorne alguma
)

# frequency_penalty = "Caso esteja dando muita resposta repetida, passar com 2"

resposta = response['choices'][0]['text'].strip()

print(resposta)