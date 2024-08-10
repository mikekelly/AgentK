from langchain_core.tools import tool

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@tool
def fetch_web_page_raw_html(url: str) -> str:
    """Fetches the raw HTML of a web page. If a CSS selector is provided, returns only the matching elements."""
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
        
    service = Service('/usr/bin/chromedriver')
    
    driver = webdriver.Chrome(options=options, service=service)

    driver.get(url)

    return driver.execute_script("return document.body.outerHTML;")