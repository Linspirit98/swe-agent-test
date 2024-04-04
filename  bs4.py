import requests
from bs4 import BeautifulSoup
url = "https://www.51cto.com/article/782625.html"


if __name__ == "__main__":
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    print(">>> scrape links",links)
    new_links = []
    for link in links:
        href = link.get('href')
        if href:
            new_links.append(href)

    parsed_url = urlparse(url)  # Parse the URL
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"  # Get the base URL
    filtered_links = [link for link in new_links if base_url in link]
    print(filtered_links)
    