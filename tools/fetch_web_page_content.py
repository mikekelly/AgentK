from langchain_core.tools import tool
from langchain_community.document_loaders.url_selenium import SeleniumURLLoader

@tool
def fetch_web_page_content(url: str):
    """Fetch content from a web page."""
    loader = SeleniumURLLoader(
        urls=[url],
        executable_path="/usr/bin/chromedriver",
        arguments=['--headless', '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']
    )
    pages = loader.load()
    
    return pages[0]