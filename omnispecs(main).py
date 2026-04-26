# ============================================================
#   Omni Specs Lookup Tool  -  Main (Requires Excel File)
#   Loads devices from your OmniSpecs Device Library.xlsx file.
#
#   How it finds the file (tries in this order):
#     1. Looks in the same folder as this script
#     2. Asks you to type the file path yourself
# ============================================================

import os
import sys
import pandas as pd


# ── VERDICT DESCRIPTIONS ────────────────────────────────────
verdict_info = {
    "Gaming": ("🎮", "Are you a gamer? This device is for you, also great for heavy work and multitasking"),
    "School": ("📚", "Works perfectly for school tasks, browsing and light productivity"),
    "Basic":  ("💡", "Best for just day-to-day tasks, remember to keep open tabs at a minimal"),
}


# FIND THE EXCEL FILE ─────────────────────────────

def find_excel_file():
    """
    Try to locate OmniSpecs Device Library.xlsx automatically.
    If it can't be found, ask the user to type the path.
    """

    # Option A: Look in the same folder as this Python script
    script_folder = os.path.dirname(os.path.abspath(__file__))
    default_path  = os.path.join(script_folder, "OmniSpecs Device Library.xlsx")

    if os.path.exists(default_path):
        print(f"  Found database: OmniSpecs Device Library.xlsx")
        return default_path

    # Option B: Ask the user to type the path themselves
    print()
    print("  Could not find 'OmniSpecs Device Library.xlsx' in the same folder as this script.")
    print()
    print("  Please type the full path to your Excel file and press Enter.")
    print("  Example (Windows) : C:\\Users\\YourName\\Documents\\OmniSpecs Device Library.xlsx")
    print("  Example (Mac/Linux): /Users/YourName/Documents/OmniSpecs Device Library.xlsx")
    print()

    while True:
        # Remove any quote marks the user might paste around the path
        typed_path = input("  Path to Excel file: ").strip().strip('"').strip("'")

        if os.path.exists(typed_path):
            print(f"  File found!")
            return typed_path
        else:
            print()
            print(f"  Could not find a file at: {typed_path}")
            print("  Please check the path and try again.")
            print()


def load_devices(file_path):
    """
    Read the Excel file and return a simple list of device rows.
    Each row is a dictionary like:
      { "Name": "iPhone 15", "RAM": 6, "Storage": 128, ... }
    """

    # Read the Excel file (row 2 is the header row in our file)
    data = pd.read_excel(file_path, header=1)

    # Remove section divider rows (they have no Name or Type)
    data = data.dropna(subset=["Name", "Type"])

    # Keep only real Phones and Laptops
    data = data[data["Type"].isin(["Phone", "Laptop"])]

    # Reset row numbers so they go 0, 1, 2, 3...
    data = data.reset_index(drop=True)

    return data


def show_device(row):
    """Print the specs for one device in a neat box."""

    name    = row["Name"]
    ram     = int(row["RAM (GB)"])
    storage = int(row["Storage (GB)"])
    screen  = row["Screen (inch)"]
    brand   = row["Brand"]

    # Figure out the verdict (Gaming / School / Basic)
    verdict_text = str(row["Quick Verdict"])
    verdict_key  = "Basic"  # default
    for key in ["Gaming", "School", "Basic"]:
        if key in verdict_text:
            verdict_key = key
            break

    emoji, description = verdict_info[verdict_key]

    # Convert storage to TB if 1024 GB or more
    if storage >= 1024:
        storage_text = f"{storage // 1024} TB"
    else:
        storage_text = f"{storage} GB"

    print()
    print("=" * 52)
    print(f"  {name}")
    print(f"  {brand}")
    print("-" * 52)
    print(f"  RAM         : {ram} GB")
    print(f"  Storage     : {storage_text}")
    print(f"  Screen Size : {screen}\"")
    print("-" * 52)
    print(f"  Quick Verdict: {emoji} {verdict_key}")
    print(f"  {description}")
    print("=" * 52)
    print()



def search_devices(data, search_term):
    """
    Look for devices whose names contain the search term.
    Returns matching rows from the data.
    Not case-sensitive, so 'iphone' finds 'iPhone'.
    """
    search_lower = search_term.lower()
    matches = data[data["Name"].str.lower().str.contains(search_lower, na=False)]
    return matches



def show_all_devices(data):
    """Print every device grouped into Phones and Laptops."""

    for device_type in ["Phone", "Laptop"]:
        icon = "📱" if device_type == "Phone" else "💻"
        group = data[data["Type"] == device_type]

        print()
        print("=" * 52)
        print(f"  {icon} {device_type.upper()}S  ({len(group)} devices)")
        print("=" * 52)

        # Group by brand so it's easier to read
        for brand in sorted(group["Brand"].unique()):
            brand_devices = group[group["Brand"] == brand]
            print(f"\n  -- {brand} --")
            for _, row in brand_devices.iterrows():
                verdict_text = str(row["Quick Verdict"])
                verdict_key  = "Basic"
                for key in ["Gaming", "School", "Basic"]:
                    if key in verdict_text:
                        verdict_key = key
                        break
                emoji = verdict_info[verdict_key][0]
                print(f"     {emoji}  {row['Name']}")

    print()


def main():
    print()
    print("=" * 52)
    print("   ⚡  Tech Specs Lookup Tool  (Excel Edition)")
    print("=" * 52)

    # Find and load the Excel file first
    file_path = find_excel_file()
    data      = load_devices(file_path)

    print()
    print(f"  {len(data)} devices loaded successfully!")
    print()
    print("  What you can type:")
    print("  - A device name (e.g. 'iPhone 15' or just 'iphone')")
    print("  - 'list'  to see all devices")
    print("  - 'quit'  to exit")
    print()

    # Keep the program running until the user types 'quit'
    while True:

        user_input = input("Search device: ").strip()

        # Skip if the user just pressed Enter without typing anything
        if user_input == "":
            continue

        # Exit the program
        if user_input.lower() in ("quit", "exit", "q"):
            print()
            print("Goodbye!")
            print()
            break

        # Show every device
        if user_input.lower() in ("list", "all"):
            show_all_devices(data)
            continue

        # Search for the device
        matches = search_devices(data, user_input)

        if len(matches) == 0:
            # Nothing found
            print()
            print(f"  No device found matching '{user_input}'.")
            print("  Try typing 'list' to see all available devices.")
            print()

        elif len(matches) == 1:
            # Exactly one match - show its full specs
            show_device(matches.iloc[0])

        else:
            # Multiple matches - list them
            print()
            print(f"  Found {len(matches)} devices matching '{user_input}':")
            print()
            for i, (_, row) in enumerate(matches.iterrows(), start=1):
                print(f"  {i}. {row['Name']}")
            print()
            print("  Tip: Type the full name to see detailed specs.")
            print()

            # If 5 or fewer matches, show all their specs automatically
            if len(matches) <= 5:
                for _, row in matches.iterrows():
                    show_device(row)


# This line makes the program start when you run the file
if __name__ == "__main__":
    main()
