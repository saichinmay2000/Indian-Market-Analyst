import faiss
import os
import pickle
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from embeddings.embedder import Embedder

class VectorStore:
    def __init__(self, persist_path="faiss_index"):
        self.persist_path = persist_path
        self.embedder = Embedder()
        self.vector_store = None

    def build_store(self, docs):
        text_docs = [Document(page_content=doc["title"] + "\n" + doc["summary"], metadata=doc) for doc in docs]
        self.vector_store = FAISS.from_documents(text_docs, self.embedder.embedding_model)
        self.vector_store.save_local(self.persist_path)

    def load_store(self):
        self.vector_store = FAISS.load_local(
        self.persist_path,
        self.embedder.embedding_model,
        allow_dangerous_deserialization=True
        )

    def search(self, query, k=5):
        if not self.vector_store:
            self.load_store()
        return self.vector_store.similarity_search(query, k=k)
