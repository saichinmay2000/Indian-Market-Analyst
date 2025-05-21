from crewai import Task
from crew.agents import scraper_agent, indexer_agent, analyst_agent

scrape_task = Task(
    description="Scrape latest news and SEBI reports about Indian companies.",
    expected_output="A list of cleaned articles with title, text, and URL.",
    agent=scraper_agent,
)

index_task = Task(
    description="Embed the scraped documents and store them in FAISS.",
    expected_output="Confirmation that documents are indexed.",
    agent=indexer_agent,
    depends_on=[scrape_task]
)

analyze_task = Task(
    description="Answer financial questions using the indexed knowledge.",
    expected_output="A detailed answer based on Indian financial data.",
    agent=analyst_agent,
    depends_on=[index_task]
)
