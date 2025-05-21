from vector_store.faiss_store import VectorStore
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

class RAGAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        self.vector_store.load_store()
        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")  # or gpt-4 if available

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_store.vector_store.as_retriever(),
            return_source_documents=True
        )

    def ask(self, question):
        result = self.qa_chain(question)
        return result["result"], result["source_documents"]
