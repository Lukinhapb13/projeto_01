import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
# MUDANÇA: Trazendo o "motor" oficial e direto do Google
from google import genai 

# A sua chave da API
chave_api = "COLA_CHAVE_AQUI"
os.environ["GOOGLE_API_KEY"] = chave_api

print("1. Lendo o documento do seu notebook...")
loader = TextLoader("material_estudo.txt", encoding="utf-8")
documento = loader.load()

print("2. Quebrando o texto em pedaços (Chunking)...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
pedacos = text_splitter.split_documents(documento)

print("3. Criando os Embeddings LOCALMENTE e salvando no Banco (Chroma)...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
banco_vetorial = Chroma.from_documents(pedacos, embeddings)

print("4. Buscando no Banco e Conectando ao LLM...")
retriever = banco_vetorial.as_retriever(search_kwargs={"k": 1})
pergunta = input("\nDigite a sua pergunta para a IA: ")
print(f"\nSua Pergunta: {pergunta}")

# O RAG em ação: Achando o pedaço exato de texto salvo no computador
pedacos_encontrados = retriever.invoke(pergunta)
contexto = pedacos_encontrados[0].page_content

# Montando a instrução final
prompt = f"Responda a pergunta baseando-se APENAS neste contexto:\n{contexto}\n\nPergunta: {pergunta}"

print("\nGerando resposta com a IA do Google (Bypass ativo)...")

# O BYPASS: Usando o cliente oficial para ignorar o bug da outra biblioteca!
cliente = genai.Client(api_key=chave_api)
resposta = cliente.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

print("\n=== RESPOSTA DA IA ===")
print(resposta.text)