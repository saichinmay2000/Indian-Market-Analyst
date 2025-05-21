from crewai import Agent, Task, Crew
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4")

# Agent 1: Scraper
scraper_agent = Agent(
    role="News Scraper",
    goal="Scrape latest Indian market news and regulatory filings",
    backstory="Expert web scraper and SEBI crawler focused on Indian finance.",
    verbose=True,
    llm=llm
)

# Agent 2: Indexer
indexer_agent = Agent(
    role="Vector Indexer",
    goal="Embed and store documents into a vector DB",
    backstory="NLP master who prepares data for semantic search.",
    verbose=True,
    llm=llm
)

# Agent 3: Analyst
analyst_agent = Agent(
    role="Financial Analyst",
    goal="Answer user queries using the indexed knowledge base",
    backstory="A financial AI who understands market trends and news.",
    verbose=True,
    llm=llm
)
