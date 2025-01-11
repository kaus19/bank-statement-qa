from llama_index.core import SimpleDirectoryReader
from PyPDF2 import PdfReader, PdfWriter
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv
import os

load_dotenv()

input_path = os.getenv("INPUT_PATH")
output_path = os.getenv("OUTPUT_PATH")
password = os.getenv("PASSWORD")

# Decrypt the PDF
def decrypt_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    if reader.is_encrypted:
        reader.decrypt(password)
    
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

decrypt_pdf(input_path, output_path, password)

documents = SimpleDirectoryReader("./data/decrypted").load_data()

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

index = VectorStoreIndex.from_documents(documents, show_progress=True)

index.storage_context.persist(persist_dir="./indexes")