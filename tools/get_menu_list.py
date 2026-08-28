import json
import re
import urllib.parse
from bs4 import BeautifulSoup
import requests

BASE_URL = "https://herremad.dk/Arkiv-Opskrifter/Opskrifter-Saesoner"
WP_BASE_URL = "https://herremadwp.herremad.dk"


def slugify(text):
    """Generates a simple URL slug/ID from Danish text."""
    text = text.lower()
    replacements = {
        "æ": "ae",
        "ø": "oe",
        "å": "aa",
        "é": "e",
        "è": "e",
        "ü": "ue",
        "ä": "ae",
        "ö": "oe",
    }
    for char, repl in replacements.items():
        text = text.replace(char, repl)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text


def parse_season_menus(start_year):
    end_year = start_year + 1
    short_start = str(start_year)[-2:]
    short_end = str(end_year)[-2:]

    # Construct the season URL structure
    season_str = f"{start_year}-{end_year}"
    page_url = f"{BASE_URL}/{season_str}/menu_{short_start}-{short_end}.htm"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(page_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(
                f"Skipping {season_str}: URL returned status {response.status_code}"
            )
            return None
    except Exception as e:
        print(f"Failed to fetch {season_str}: {e}")
        return None

    # Handle encoding issues often present in HTML from Microsoft FrontPage
    response.encoding = response.apparent_encoding or "windows-1252"
    soup = BeautifulSoup(response.text, "html.parser")

    menu_list = []

    # Locate the main data table
    tables = soup.find_all("table")
    data_table = None

    for table in tables:
        # Tables usually contain header texts like FORRET or HOVEDRET
        text_content = table.get_text()
        if "HOVEDRET" in text_content or "FORRET" in text_content:
            data_table = table
            break

    if not data_table:
        print(f"Could not locate menu table for {season_str}")
        return None

    rows = data_table.find_all("tr")

    for row in rows:
        cols = row.find_all(["td", "th"])
        if len(cols) < 3:
            continue

        date_text = cols[0].get_text(strip=True)

        # Match date pattern like 01. okt. 2024 or 01.10.2024
        date_match = re.search(r"(\d{2})[\.\/\s]+([^\s\d]+|\d{2})[\.\/\s]+(\d{4})", date_text)
        if not date_match:
            continue

        day, month, year = date_match.groups()

        # Convert month name to two-digit format if necessary
        month_map = {
            "jan": "01",
            "feb": "02",
            "mar": "03",
            "apr": "04",
            "maj": "05",
            "jun": "06",
            "jul": "07",
            "aug": "08",
            "sep": "09",
            "okt": "10",
            "nov": "11",
            "dec": "12",
        }
        month_clean = month.lower().replace(".", "")
        if month_clean in month_map:
            month = month_map[month_clean]

        formatted_date = f"{day.zfill(2)}.{month.zfill(2)}.{year}"
        date_slug = f"{day.zfill(2)}-{month.zfill(2)}-{year}"
        menu_link = f"{WP_BASE_URL}/{date_slug}-menu/"

        recipes = []
        course_types = ["forret", "hovedret", "dessert"]

        for idx, col in enumerate(cols[1:4]):
            if idx >= len(course_types):
                break

            recipe_name = col.get_text(strip=True)
            # Filter empty cells or structural noise
            if not recipe_name or recipe_name in ["&nbsp;", "-"]:
                continue

            recipe_id = slugify(recipe_name)
            if not recipe_id:
                recipe_id = "menu"

            recipe_link = f"{WP_BASE_URL}/{date_slug}-{recipe_id}/"

            recipes.append(
                {
                    "name": recipe_name,
                    "ID": recipe_id,
                    "Link": recipe_link,
                    "type": course_types[idx],
                }
            )

        if recipes:
            menu_list.append(
                {"date": formatted_date, "Link": menu_link, "recipes": recipes}
            )

    return menu_list


def main():
    # Iterate through start years from 2005 to 2025 (covering season 2025-2026)
    for year in range(2005, 2026):
        data = parse_season_menus(year)
        if data:
            filename = f"herremad_datoer_{year}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent="\t")
            print(f"Successfully generated {filename}")


if __name__ == "__main__":
    main()