"""Generate 9 symbol emblems via Bria AI — distinct relevant colour per symbol.

Each emblem is a centered subject on a clean light background so it cuts out
cleanly (RMBG) for compositing into a CONSISTENT card template.
Square (1:1) format keeps every symbol the same shape for consistent placement.

Colour identities (distinct + thematically relevant, per deck-structure.md):
  1 Void  - deep indigo/violet (cosmic emptiness)
  2 Root  - earthy green/brown (living wood)
  3 Wave  - ocean blue/cyan (water)
  4 Flame - red/orange (fire)
  5 Eye   - teal/emerald (sight, wisdom)
  6 Mask  - purple/magenta (mystery, theatre)
  7 Key   - gold/amber (metal, unlocking)
  8 Star  - bright yellow/white (celestial light)
  9 Crown - royal purple + gold (sovereignty)
"""

import requests
import time
import os

API_KEY = "fd37cb947b5e42b7a192d7c504fc9762"
BASE_URL = "https://engine.prod.bria-api.com"
HEADERS = {
    "api_token": API_KEY,
    "Content-Type": "application/json",
    "User-Agent": "BriaSkills/1.3.4",
}

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Shared style — bold filled emblem on clean off-white background, centered.
# Light background makes background-removal clean for compositing.
STYLE = (
    "A single bold centered emblem icon on a plain solid off-white background. "
    "Bold filled high-contrast vector illustration, clean modern flat design with "
    "subtle shading, symmetrical and centered, the emblem fills the central area "
    "with even margins on all sides. Strong silhouette, vivid saturated colour. "
    "No border, no frame, no text, no words, no letters, no numbers, no drop shadow."
)

# (name, colour description, subject description)
SIGNS = {
    1: ("Void", "deep indigo and violet with a dark cosmic centre",
        "a cosmic void: a dark indigo circle ringed by glowing violet light, "
        "faint concentric rings suggesting infinite emptiness"),
    2: ("Root", "rich earthy green and warm brown",
        "an ancient sacred tree with symmetrical spreading roots below and bare branches above"),
    3: ("Wave", "vivid ocean blue and bright cyan with white foam",
        "three stacked cresting ocean waves in a stylized symmetrical motif, Japanese wave style"),
    4: ("Flame", "vivid red, orange and yellow",
        "a single elegant flame rising upward, symmetrical, glowing hot fire"),
    5: ("Eye", "vibrant teal and emerald green",
        "a single all-seeing eye, almond-shaped with a radiant detailed iris"),
    6: ("Mask", "rich purple and magenta",
        "an elegant theatrical masquerade mask, symmetrical, with hollow eye holes, ornate detail"),
    7: ("Key", "polished gold and warm amber",
        "an ornate antique skeleton key standing vertically with a decorative bow"),
    8: ("Star", "brilliant golden yellow and white",
        "a radiant eight-pointed star with sharp rays, symmetrical, shining bright"),
    9: ("Crown", "royal purple and gold",
        "a majestic five-pointed royal crown with jewels, symmetrical and regal"),
}


def generate_image(prompt, aspect_ratio="1:1"):
    body = {"prompt": prompt, "aspect_ratio": aspect_ratio, "num_results": 1}
    resp = requests.post(f"{BASE_URL}/v2/image/generate", headers=HEADERS, json=body)
    resp.raise_for_status()
    data = resp.json()
    if "result" in data and "image_url" in data.get("result", {}):
        return ("done", data["result"]["image_url"])
    return ("poll", data["status_url"])


def poll_status(status_url, timeout=180):
    for _ in range(timeout // 3):
        resp = requests.get(status_url, headers=HEADERS)
        data = resp.json()
        status = data.get("status", "")
        if status == "COMPLETED":
            return data["result"]["image_url"]
        if status == "FAILED":
            raise Exception(f"Generation failed: {data}")
        time.sleep(3)
    raise TimeoutError(f"Timeout polling {status_url}")


def download_image(url, filepath):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)


def main():
    print("Generating 9 symbol emblems via Bria AI (distinct colours, clean bg)...\n")
    for pip, (name, colour, desc) in SIGNS.items():
        prompt = f"{STYLE} The emblem depicts {desc}, rendered in {colour}."
        filename = f"emblem_{pip:02d}_{name.lower()}.png"
        filepath = os.path.join(OUT_DIR, filename)
        print(f"  [{pip}/9] {name} ({colour.split(' and ')[0]})... ", end="", flush=True)
        try:
            result_type, result = generate_image(prompt)
            image_url = poll_status(result) if result_type == "poll" else result
            download_image(image_url, filepath)
            print(f"done -> {filename}")
        except Exception as e:
            print(f"FAILED: {e}")
    print("\nDone! Emblems saved.")


if __name__ == "__main__":
    main()
