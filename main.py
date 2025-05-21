from scrapers.news_scraper import scrape_all_news
from scrapers.sebi_scraper import scrape_sebi_press_releases
from vector_store.faiss_store import VectorStore
from rag_pipeline.rag_agent import RAGAgent
from dotenv import load_dotenv
load_dotenv()

def main():
    print("🔎 Scraping latest articles...")
    news = scrape_all_news()
    # sebi = scrape_sebi_press_releases()
    all_data = news

    print(f"🧠 Embedding {len(all_data)} articles...")
    vs = VectorStore()
    vs.build_store(all_data)
    print("✅ Stored in FAISS.")

    # Try querying
    results = vs.search("What happened with Infosys?")
    print("\n🔍 Top Matches:\n")
    for doc in results:
        print(doc.metadata['title'])
        print(doc.metadata['url'])
        print("---")
    
    rag = RAGAgent()
    query = "Summarize recent news about Mahindra"
    response, sources = rag.ask(query)

    print("\n🤖 Answer:\n")
    print(response)

    print("\n📚 Sources:")
    for src in sources:
        print("-", src.metadata["title"])

if __name__ == "__main__":
    main()
