#!/usr/bin/env python3
"""Searchable source-documented vocabulary library for Lepcha, Rai varieties, and Tamang."""
import json, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
JSON_FILE = DATA / "vocabulary.json"
CSV_FILE = DATA / "vocabulary.csv"
FIELDS = [
    "english", "lepcha", "rai", "tamang", "part_of_speech", "dialect",
    "notes", "source", "source_url", "page_reference", "verified_by"
]
LANGUAGES = ("Lepcha", "Rai", "Tamang")

def load_entries():
    DATA.mkdir(exist_ok=True)
    if not JSON_FILE.exists():
        JSON_FILE.write_text("[]", encoding="utf-8")
    try:
        items = json.loads(JSON_FILE.read_text(encoding="utf-8"))
        return items if isinstance(items, list) else []
    except (OSError, json.JSONDecodeError):
        print("Could not read data/vocabulary.json. Please check the file format.")
        return []

def save_entries(entries):
    JSON_FILE.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    with CSV_FILE.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows({k: item.get(k, "") for k in FIELDS} for item in entries)

def show_entry(item, number=None):
    if number is not None:
        print(f"\n{number}. ", end="")
    print(item.get("english", "(no English headword)"))
    for language in LANGUAGES:
        print(f"  {language}: {item.get(language.lower()) or '—'}")
    for key, label in [
        ("dialect", "Variety/dialect"), ("part_of_speech", "Part of speech"),
        ("source", "Source"), ("source_url", "Source URL"),
        ("page_reference", "Page/reference"), ("verified_by", "Verified by"),
        ("notes", "Notes")
    ]:
        if item.get(key):
            print(f"  {label}: {item[key]}")

def search(entries):
    term = input("Search word, translation, dialect, or source: ").strip().casefold()
    found = [e for e in entries if term and any(term in str(v).casefold() for v in e.values())]
    if not found:
        print("No matching entries.")
    for i, item in enumerate(found, 1):
        show_entry(item, i)

def add(entries):
    print("\nAdd a verified vocabulary item. Leave unknown translations blank.")
    item = {}
    item["english"] = input("English word/phrase (required): ").strip()
    if not item["english"]:
        print("English word/phrase is required.")
        return
    item["lepcha"] = input("Lepcha: ").strip()
    item["rai"] = input("Rai variety translation (if known): ").strip()
    item["tamang"] = input("Tamang: ").strip()
    item["part_of_speech"] = input("Part of speech: ").strip()
    item["dialect"] = input("Exact variety/dialect (especially for Rai): ").strip()
    item["source"] = input("Book/dictionary/speaker source: ").strip()
    item["source_url"] = input("Source URL (if available): ").strip()
    item["page_reference"] = input("Page number or entry reference: ").strip()
    item["verified_by"] = input("Verified by (optional): ").strip()
    item["notes"] = input("Notes / spelling variants: ").strip()
    entries.append(item)
    save_entries(entries)
    print("Saved to JSON and CSV.")

def show_sources():
    path = DATA / "sources.json"
    if not path.exists():
        print("See sources/RESEARCH_NOTES.md for source links.")
        return
    for i, item in enumerate(json.loads(path.read_text(encoding="utf-8")), 1):
        print(f"\n{i}. [{item['language']}] {item['title']}")
        print(f"   {item['url']}")
        print(f"   {item['notes']}")

def main():
    entries = load_entries()
    save_entries(entries)
    while True:
        print("\n" + "=" * 48)
        print("LEPCHA • RAI • TAMANG LANGUAGE LIBRARY")
        print("=" * 48)
        print(f"Vocabulary entries: {len(entries)}")
        print("1. Search vocabulary")
        print("2. Add verified vocabulary")
        print("3. View all vocabulary")
        print("4. Export/update CSV")
        print("5. View research sources")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()
        if choice == "1":
            search(entries)
        elif choice == "2":
            add(entries)
        elif choice == "3":
            for i, item in enumerate(entries, 1): show_entry(item, i)
            if not entries: print("No vocabulary yet. Check sources and add verified entries.")
        elif choice == "4":
            save_entries(entries); print(f"CSV updated: {CSV_FILE}")
        elif choice == "5":
            show_sources()
        elif choice == "6":
            print("Goodbye!"); break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
