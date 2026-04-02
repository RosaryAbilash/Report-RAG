from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Data Ingestion
loader = PyPDFLoader("report.pdf")
documents = loader.load()

# Chuncking with Default Chunck Size and Overlap
splitter = RecursiveCharacterTextSplitter()
chuncks = splitter.split_documents(documents)


# Embedding
embedding = HuggingFaceEmbeddings(
    model_name="../models/all-MiniLM-L6-v2"
)

# FAISS Vector DB
vectorDB = FAISS.from_documents(chuncks, embedding)

# Saving VectorDB
vectorDB.save_local("Faiss_Report")