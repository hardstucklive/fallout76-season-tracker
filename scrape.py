import requests
from bs4 import BeautifulSoup

URL = "https://fallout.wiki/wiki/Season_17"

def fetch_season_end():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    infobox = soup.find("table", class_="infobox")
    if infobox:
        rows = infobox.find_all("tr")
        for row in rows:
            if "End date" in row.text:
                date_cell = row.find("td")
                if date_cell:
                    date = date_cell.text.strip()
                    return f"Fallout 76 Season 17 ends on {date}."

    return "Could not fetch season end date."

# Write to file
with open("season.txt", "w") as file:
    file.write(fetch_season_end())
