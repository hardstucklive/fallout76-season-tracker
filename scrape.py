import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fallout.wiki/wiki/Seasons"
BASE_DOMAIN = "https://fallout.wiki"

def get_latest_season_url():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first link that looks like a season page
    for link in soup.find_all("a"):
        href = link.get("href", "")
        if href.startswith("/wiki/Season_") and href[-2:].isdigit():
            return BASE_DOMAIN + href
    return None

def fetch_season_end():
    season_url = get_latest_season_url()
    if not season_url:
        return "Could not find latest season page."

    response = requests.get(season_url)
    soup = BeautifulSoup(response.content, "html.parser")

    infobox = soup.find("table", class_="infobox")
    if infobox:
        for row in infobox.find_all("tr"):
            if "End date" in row.text:
                td = row.find("td")
                if td:
                    date = td.text.strip()
                    return f"Fallout 76 season ends on {date}."
    return "Could not fetch season end date."

# Write to file
with open("season.txt", "w") as file:
    file.write(fetch_season_end())
