import requests
from bs4 import BeautifulSoup

def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extracting text from the page, customized based on structure of the article pages
            paragraphs = soup.find_all('p')
            content = '\n'.join([para.get_text() for para in paragraphs])
            return content
        else:
            print(f"Failed to retrieve {url}, Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
