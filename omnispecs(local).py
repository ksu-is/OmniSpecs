# ============================================================
#   Omni Specs Lookup Tool  -  Local (Built-in Library)
#   No external files needed. All devices are listed below.
#   Just run this file and start searching!
# ============================================================

# ── DEVICE LIBRARY ──────────────────────────────────────────
# Each device follows this format:
#   "Device Name": [RAM (GB), Storage (GB), Screen (inches), Verdict]
# Verdict choices: "Gaming", "School", "Basic"
# To add a new device, just copy any line below and change the values.

devices = {

    # ── iPHONES ─────────────────────────────────────────────
    "iPhone 6":             [1,   16,   4.7,  "Basic"],
    "iPhone 6 Plus":        [1,   16,   5.5,  "Basic"],
    "iPhone 6s":            [2,   16,   4.7,  "Basic"],
    "iPhone 6s Plus":       [2,   16,   5.5,  "Basic"],
    "iPhone 7":             [2,   32,   4.7,  "Basic"],
    "iPhone 7 Plus":        [3,   32,   5.5,  "School"],
    "iPhone 8":             [2,   64,   4.7,  "Basic"],
    "iPhone 8 Plus":        [3,   64,   5.5,  "School"],
    "iPhone X":             [3,   64,   5.8,  "School"],
    "iPhone XR":            [3,   64,   6.1,  "School"],
    "iPhone XS":            [4,   64,   5.8,  "School"],
    "iPhone XS Max":        [4,   64,   6.5,  "School"],
    "iPhone 11":            [4,   64,   6.1,  "School"],
    "iPhone 11 Pro":        [4,   64,   5.8,  "School"],
    "iPhone 11 Pro Max":    [4,   64,   6.5,  "School"],
    "iPhone 12":            [4,   64,   6.1,  "School"],
    "iPhone 12 Mini":       [4,   64,   5.4,  "School"],
    "iPhone 12 Pro":        [6,  128,   6.1,  "School"],
    "iPhone 12 Pro Max":    [6,  128,   6.7,  "Gaming"],

    # ── SAMSUNG GALAXY S SERIES ─────────────────────────────
    "Samsung Galaxy S10":           [8,  128,  6.1,  "School"],
    "Samsung Galaxy S10+":          [8,  128,  6.4,  "School"],
    "Samsung Galaxy S20":           [8,  128,  6.2,  "Gaming"],
    "Samsung Galaxy S20 Ultra":     [12, 128,  6.9,  "Gaming"],
    "Samsung Galaxy S21":           [8,  128,  6.2,  "Gaming"],
    "Samsung Galaxy S21 Ultra":     [12, 128,  6.8,  "Gaming"],
    "Samsung Galaxy S22":           [8,  128,  6.1,  "Gaming"],
    "Samsung Galaxy S22 Ultra":     [12, 128,  6.8,  "Gaming"],
    "Samsung Galaxy S23":           [8,  128,  6.1,  "Gaming"],
    "Samsung Galaxy S23 Ultra":     [12, 256,  6.8,  "Gaming"],
    "Samsung Galaxy S24":           [8,  128,  6.2,  "Gaming"],
    "Samsung Galaxy S24 Ultra":     [12, 256,  6.9,  "Gaming"],
    "Samsung Galaxy S25":           [12, 128,  6.2,  "Gaming"],
    "Samsung Galaxy S25 Ultra":     [12, 256,  6.9,  "Gaming"],

    # ── NOKIA ───────────────────────────────────────────────
    "Nokia G42 5G":                 [6,  128,  6.56, "School"],
    "Nokia G22":                    [4,   64,  6.52, "Basic"],
    "Nokia XR21":                   [6,  128,  6.49, "School"],
    "Nokia C32":                    [4,   64,  6.5,  "Basic"],

    # ── GOOGLE PIXEL ────────────────────────────────────────
    "Google Pixel 9":               [12, 128,  6.3,  "Gaming"],
    "Google Pixel 9 Pro":           [16, 128,  6.3,  "Gaming"],
    "Google Pixel 8a":              [8,  128,  6.1,  "School"],
    "Google Pixel 7a":              [8,  128,  6.1,  "School"],

    # ── HP LAPTOPS ──────────────────────────────────────────
    "HP EliteBook 840 G11":         [32,  512, 14.0, "School"],
    "HP EliteBook 860 G11":         [32,  512, 16.0, "School"],
    "HP ProBook 440 G11":           [8,   256, 14.0, "School"],
    "HP ProBook 450 G11":           [16,  512, 15.6, "School"],
    "HP Omen 16 (2024)":            [16,  512, 16.1, "Gaming"],
    "HP Omen Max 16":               [32, 1024, 16.0, "Gaming"],
    "HP Victus 15 (2024)":          [16,  512, 15.6, "Gaming"],
    "HP Spectre x360 14 (2024)":    [32, 2048, 13.5, "Gaming"],
    "HP Envy x360 15 (2024)":       [16,  512, 15.6, "School"],
    "HP Pavilion 15 (2024)":        [8,   512, 15.6, "School"],

    # ── DELL LAPTOPS ────────────────────────────────────────
    "Dell XPS 13 (2024)":           [32,  512, 13.4, "School"],
    "Dell XPS 14 (2024)":           [32,  512, 14.5, "Gaming"],
    "Dell XPS 16 (2024)":           [64, 1024, 16.3, "Gaming"],
    "Dell Inspiron 14 Plus":        [32, 1024, 14.0, "School"],
    "Dell Inspiron 15 3000":        [8,   512, 15.6, "Basic"],
    "Dell Latitude 9440":           [16,  512, 14.0, "School"],
    "Dell Alienware m18 R2":        [32, 1024, 18.0, "Gaming"],
    "Dell Alienware x16 R2":        [32, 1024, 16.0, "Gaming"],
    "Dell G15 Gaming (2024)":       [16,  512, 15.6, "Gaming"],
    "Dell G16 Gaming (2024)":       [16,  512, 16.0, "Gaming"],

        # ── APPLE MacBook ────────────────────────────────────────
    "MacBook Air M2 13":            [8,   256, 13.6, "School"],
    "MacBook Air M3 13":            [8,   256, 13.6, "School"],
    "MacBook Air M3 15":            [8,   256, 15.3, "School"],
    "MacBook Pro M3 14":            [18,  512, 14.2, "Gaming"],
    "MacBook Pro M3 Max 16":        [36, 1024, 16.2, "Gaming"],

}

# ── VERDICT DESCRIPTIONS ────────────────────────────────────
# What each verdict means and which emoji to show
verdict_info = {
    "Gaming": ("🎮", "Are you a gamer? This device is for you, also great for heavy work and multitasking"),
    "School": ("📚", "Works perfectly for school tasks, browsing and light productivity"),
    "Basic":  ("💡", "Best for just day-to-day tasks, remember to keep open tabs at a minimal"),
}


# ── HELPER FUNCTIONS ────────────────────────────────────────

def show_device(name, specs):
    """Print the specs for one device in a neat box."""
    ram, storage, screen, verdict = specs
    emoji, description = verdict_info[verdict]

    # Convert storage to TB if it's 1024 GB or more
    if storage >= 1024:
        storage_text = f"{storage // 1024} TB"
    else:
        storage_text = f"{storage} GB"

    print()
    print("=" * 50)
    print(f"  {name}")
    print("-" * 50)
    print(f"  RAM         : {ram} GB")
    print(f"  Storage     : {storage_text}")
    print(f"  Screen Size : {screen}\"")
    print("-" * 50)
    print(f"  Quick Verdict: {emoji} {verdict}")
    print(f"  {description}")
    print("=" * 50)
    print()


def search_devices(search_term):
    
    search_lower = search_term.lower()
    matches = []
    for device_name in devices:
        if search_lower in device_name.lower():
            matches.append(device_name)
    return matches


def show_all_devices():
    """Print every device in the library, grouped into Phones and Laptops."""
   
    phones  = {n: s for n, s in devices.items() if s[2] < 8}
    laptops = {n: s for n, s in devices.items() if s[2] >= 8}

    print()
    print("=" * 50)
    print("  📱 PHONES")
    print("=" * 50)
    for name, specs in phones.items():
        emoji = verdict_info[specs[3]][0]
        print(f"  {emoji}  {name}")

    print()
    print("=" * 50)
    print("  💻 LAPTOPS")
    print("=" * 50)
    for name, specs in laptops.items():
        emoji = verdict_info[specs[3]][0]
        print(f"  {emoji}  {name}")
    print()


# ── MAIN PROGRAM ────────────────────────────────────────────

def main():
    print()
    print("=" * 50)
    print("   ⚡  Tech Specs Lookup Tool")
    print(f"   {len(devices)} devices in the built-in library")
    print("=" * 50)
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
            show_all_devices()
            continue

        # Search for the device
        matches = search_devices(user_input)

        if len(matches) == 0:
            # Nothing found
            print()
            print(f"  No device found matching '{user_input}'.")
            print("  Try typing 'list' to see all available devices.")
            print()

        elif len(matches) == 1:
            # Exactly one match - show its full specs
            device_name = matches[0]
            show_device(device_name, devices[device_name])

        else:
            # Multiple matches found - list them all
            print()
            print(f"  Found {len(matches)} devices matching '{user_input}':")
            print()
            for i, name in enumerate(matches, start=1):
                print(f"  {i}. {name}")
            print()
            print("  Tip: Type the full name to see detailed specs.")
            print()


if __name__ == "__main__":
    main()

