import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file):
    try:
        # Step 1: Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
        html_content = response.text

        # Step 2: Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Step 3: Extract headlines (common tags: h1, h2, h3)
        headlines = []
        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)
            if text and len(text.split()) > 2:  # filter short/uninformative text
                headlines.append(text)

        # Step 4: Save headlines to file
        with open(output_file, "w", encoding="utf-8") as file:
            for line in headlines:
                file.write(line + "\n")

        print(f"✅ {len(headlines)} headlines saved to {output_file}")

    except requests.RequestException as e:
        print("❌ Error fetching the website:", e)

if __name__ == "__main__":
    # Example: BBC News website
    news_url = "https://www.bbc.com/news"
    output_filename = "headlines.txt"
    scrape_headlines(news_url, output_filename)
