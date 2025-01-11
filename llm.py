from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
Settings.llm = Ollama(model="llama3", request_timeout=300.0)

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./indexes")

# load index
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query(
    "What is the data about?"
)
print(response)