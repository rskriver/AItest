import json
import os
import re

# Set the path to the folder containing your JSON files
FOLDER_PATH = "."


def clean_string(text: str) -> str:
    """Removes line breaks, tabs, and collapses multiple spaces into one."""
    if not isinstance(text, str):
        return text

    # Replace newlines, tabs, and carriage returns with a single space
    cleaned = re.sub(r"[\n\r\t]+", " ", text)
    # Collapse multiple consecutive spaces into a single space and strip edges
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def clean_json_data(data):
    """Recursively traverses JSON data (dicts, lists) to clean all string keys and values."""
    if isinstance(data, dict):
        return {
            clean_string(k): clean_json_data(v) for k, v in data.items()
        }
    elif isinstance(data, list):
        return [clean_json_data(item) for item in data]
    elif isinstance(data, str):
        return clean_string(data)
    else:
        return data


def process_json_files(folder_path: str):
    """Finds all .json files in the folder and cleans whitespace formatting."""
    if not os.path.exists(folder_path):
        print(f"Error: Folder path '{folder_path}' does not exist.")
        return

    count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    cleaned_data = clean_json_data(data)

                    with open(file_path, "w", encoding="utf-8") as f:
                        # ensure_ascii=False preserves characters like æ, ø, å
                        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

                    print(f"Cleaned: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"\nFinished! Cleaned {count} JSON file(s).")


if __name__ == "__main__":
    process_json_files(FOLDER_PATH)