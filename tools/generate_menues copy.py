import json
import os
import re
import requests
from bs4 import BeautifulSoup

def convert_date_format(date_str):
    """Converts DD.MM.YYYY to YYYY-MM-DD."""
    parts = date_str.split(".")
    if len(parts) == 3:
        return f"{parts[2]}-{parts[1]}-{parts[0]}"
    return date_str

def fetch_soup(url):
    """Fetches web page content with a standard user-agent header."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_image_url(soup):
    """Extracts main featured image or open graph image."""
    og_image = soup.find("meta", property="og:image")
    if og_image and og_image.get("content"):
        return og_image["content"]
    
    img = soup.find("img", class_=re.compile(r"wp-post-image|featured-image|entry-thumb"))
    if img and img.get("src"):
        return img["src"]
        
    return ""

def parse_recipe_page(url):
    """Scrapes ingredients, methods, image, and metadata from individual recipe pages."""
    soup = fetch_soup(url)
    if not soup:
        return None

    recipe_data = {
        "serves": 4,
        "ingredients": [],
        "method": []
    }

    # Extract serving count if present (e.g., "Personer: 4" or "4 personer")
    page_text = soup.get_text()
    serves_match = re.search(r"(\d+)\s*(?:personer|portioner)", page_text, re.IGNORECASE)
    if serves_match:
        recipe_data["serves"] = int(serves_match.group(1))

    # Parse Ingredients Sections
    ing_containers = soup.find_all(class_=re.compile(r"ingredient|ingredienser", re.I))
    if ing_containers:
        for container in ing_containers:
            label = None
            header = container.find(['h2', 'h3', 'h4', 'strong'])
            if header:
                label = header.get_text(strip=True)
            
            items = [li.get_text(strip=True) for li in container.find_all("li") if li.get_text(strip=True)]
            if items:
                recipe_data["ingredients"].append({"label": label, "items": items})

    # Fallback ingredient parser if no explicit containers exist
    if not recipe_data["ingredients"]:
        default_items = []
        for ul in soup.find_all("ul"):
            for li in ul.find_all("li"):
                text = li.get_text(strip=True)
                if text and len(text) < 100:
                    default_items.append(text)
        if default_items:
            recipe_data["ingredients"].append({"label": None, "items": default_items})

    # Parse Method Steps
    method_containers = soup.find_all(class_=re.compile(r"instructions|method|fremgangsmaade|opskrift", re.I))
    if method_containers:
        for container in method_containers:
            label = None
            header = container.find(['h2', 'h3', 'h4', 'strong'])
            if header:
                label = header.get_text(strip=True)
            
            steps = [li.get_text(strip=True) for li in container.find_all("li") if li.get_text(strip=True)]
            if not steps:
                steps = [p.get_text(strip=True) for p in container.find_all("p") if p.get_text(strip=True)]
            
            if steps:
                recipe_data["method"].append({"label": label, "steps": steps})

    # Fallback method parser using ordered lists
    if not recipe_data["method"]:
        default_steps = []
        for ol in soup.find_all("ol"):
            for li in ol.find_all("li"):
                text = li.get_text(strip=True)
                if text:
                    default_steps.append(text)
        if default_steps:
            recipe_data["method"].append({"label": None, "steps": default_steps})

    return recipe_data

def process_menu_file(input_filename):
    """Reads master JSON file and outputs 1 JSON file per date."""
    if not os.path.exists(input_filename):
        print(f"File {input_filename} not found.")
        return

    with open(input_filename, "r", encoding="utf-8") as f:
        menu_dates = json.load(f)

    for entry in menu_dates:
        raw_date = entry.get("date")
        date_iso = convert_date_format(raw_date)
        menu_url = entry.get("Link")
        
        print(f"\nProcessing menu for date: {raw_date} ({date_iso})...")

        # Fetch menu landing page for header background/main image
        main_image = ""
        if menu_url:
            soup = fetch_soup(menu_url)
            if soup:
                main_image = extract_image_url(soup)

        dishes = []
        for recipe in entry.get("recipes", []):
            course_name = recipe.get("name")
            course_id = recipe.get("ID")
            course_type = recipe.get("type", "").capitalize()
            course_link = recipe.get("Link")

            print(f" -> Scraping course: {course_name}")
            
            scraped_details = parse_recipe_page(course_link) if course_link else None

            dish_entry = {
                "id": course_id,
                "name": course_name,
                "type": course_type,
                "serves": scraped_details.get("serves", 4) if scraped_details else 4,
                "ingredients": scraped_details.get("ingredients", []) if scraped_details else [],
                "method": scraped_details.get("method", []) if scraped_details else []
            }
            dishes.append(dish_entry)

        # Build output structure matching 24-03-2026.json design
        output_payload = {
            "menu": {
                "title": "Foreningen HERREMAD",
                "date": date_iso,
                "image": main_image,
                "dishes": dishes
            }
        }

        # Write output file per date (formatted as DD-MM-YYYY.json)
        output_filename = f"{raw_date.replace('.', '-')}.json"
        with open(output_filename, "w", encoding="utf-8") as out_file:
            json.dump(output_payload, out_file, ensure_ascii=False, indent=4)
            
        print(f"Saved: {output_filename}")

if __name__ == "__main__":
    # Ensure external dependencies are installed:
    # pip install requests beautifulsoup4
    process_menu_file("herremad_datoer_2024.json")