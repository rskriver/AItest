import datetime
import json
import os
import sys


def date_to_iso(date_str):
    """Converts a date string from DD.MM.YYYY format to YYYY-MM-DD."""
    dt = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    return dt.strftime("%Y-%m-%d")


def generate_recipe_jsons(input_filepath, output_dir="."):
    """Reads a menu list file and creates a recipe JSON file for each date."""
    with open(input_filepath, "r", encoding="utf-8") as f:
        menu_list = json.load(f)

    os.makedirs(output_dir, exist_ok=True)

    for menu_entry in menu_list:
        raw_date = menu_entry.get("date")
        if not raw_date:
            continue

        # Format date for the output payload and filename
        iso_date = date_to_iso(raw_date)

        dishes = []
        for recipe in menu_entry.get("recipes", []):
            dishes.append(
                {
                    "id": recipe.get("ID"),
                    "name": recipe.get("name"),
                    "type": recipe.get("type", "").capitalize(),
                    "serves": 4,  # Default value based on target structure
                    "ingredients": [
                        {"label": None, "items": []}
                    ],  # Placeholder for ingredients list
                    "method": [
                        {"label": None, "steps": []}
                    ],  # Placeholder for preparation steps
                }
            )

        # Structure matching the single menu JSON file standard
        menu_json = {
            "menu": {
                "title": "Foreningen HERREMAD",
                "date": iso_date,
                "image": "https://herremadwp.herremad.dk/wp-content/uploads/2025/07/hl1.jpg",
                "dishes": dishes,
            }
        }

        # Write output file named after the ISO date format
        output_filename = os.path.join(output_dir, f"{iso_date}.json")
        with open(output_filename, "w", encoding="utf-8") as out_file:
            json.dump(menu_json, out_file, ensure_ascii=False, indent=4)

        print(f"Created menu file: {output_filename}")


# if __name__ == "__main__":
#     # Replace 'menu_list.json' with your input file path
#     generate_recipe_jsons("menu_list.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_menus.py <path_to_menu_list.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    generate_recipe_jsons(input_file)