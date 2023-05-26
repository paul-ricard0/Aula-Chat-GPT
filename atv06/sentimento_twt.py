import pandas as pd
import re, os
import openai
import json
import string

# Vamos diminuir a quantidade de linhas!!!!!!!
df = pd.read_parquet(r'.\data\dados_twt.parquet')
df = df.head(5) 

# Obtenha os nomes das colunas do DataFrame original
columns = df.columns.tolist()
# Adicionando nova coluna
columns.append('sentimento_gpt') 
df_coleta = pd.DataFrame(columns=columns)

for index, row in df.iterrows():
    tweet = row['text']

    # Forma regex para excluir o inicio do rt
    padrao_rt = r'rt @\w+:'  
    # Excluindo a parte do rt
    tweet_limpo = re.sub(padrao_rt, '', tweet).strip() 
    
    # API_OPENAI
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = "Responda em ÚNICA palavra, sendo positivo, negativo ou neutro o sentimento do seguinte texto: "+ tweet_limpo
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature= 0.7,
        max_tokens= 10,
        n=1, 
        stop=None 
    )
    
    # Passo 1: Pegando response a resposta 
    choices = response["choices"][0] 
    data_dict = json.loads(str(choices))
    resposta = data_dict['text']

    # Passo 2: Remove pontos e vírgulas
    tabela_punctuation = str.maketrans('', '', string.punctuation)
    frase_sem_pontuacao = resposta.translate(tabela_punctuation)

    # Passo 3: Transformando a frase em uma lista com base no espaço entre as palavras
    tokens = frase_sem_pontuacao.strip().split()

    # Passo 4: Seleção de palavras-chave
    palavras_chave = ['neutro', 'positivo', 'negativo']
    palavras_selecionadas = [token for token in tokens if token.lower() in palavras_chave]
    
    # Passo 5: Juntar as palavras selecionadas
    sentimento_gpt = ''.join(palavras_selecionadas)
    
    df_coleta.loc[len(df_coleta)] = [tweet, row['sentimento_google'], row['toxicity_score_google'], row['senti'], row['nota_senticnet_scaler'], sentimento_gpt]

# Tirando o score
df_final = df_coleta.drop(df.columns[[2,4]], axis=1)
print(df_final)