from crewai import Crew
from crew.tasks import scrape_task, index_task, analyze_task
from crew.agents import scraper_agent, indexer_agent, analyst_agent

def run_crew(query):
    crew = Crew(
        agents=[scraper_agent, indexer_agent, analyst_agent],
        tasks=[scrape_task, index_task, analyze_task],
        verbose=True
    )

    results = crew.kickoff(inputs={"query": query})
    return results
