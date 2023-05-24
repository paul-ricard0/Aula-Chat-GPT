import dotenv # Carregar o arquivo .env
import os # utilizar var ambientes


dotenv.load_dotenv()

chave = os.getenv("KEY")

print(chave)