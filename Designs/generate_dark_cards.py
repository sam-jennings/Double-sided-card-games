"""Generate 9 card designs via Bria AI in a dark mystical tarot style.

Inspired by the ChatGPT reference: dark/black backgrounds, warm gold/amber
ornate artwork, mystical atmospheric aesthetic. Each card is a complete
face design at 3:4 aspect ratio (portrait card format).

These are generated as FULL card face designs (not just icons to composite),
letting Bria handle the complete artistic composition.
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

# Style prefix shared by all prompts — dark mystical card design
STYLE = (
    "Dark mystical tarot card design with black background, "
    "ornate gold filigree border frame, "
    "moody atmospheric lighting, "
    "elegant occult aesthetic, "
    "high contrast with warm amber and gold accents against deep black. "
    "Professional card game art, vertical portrait format. "
    "No text, no words, no letters, no numbers."
)

SIGNS = {
    1: {
        "name": "Void",
        "prompt": (
            f"{STYLE} "
            "Central symbol: a dark cosmic void portal — a perfect circle of absolute darkness "
            "surrounded by a ring of faint indigo light, suggesting infinite emptiness and the absence of all things. "
            "Ethereal dark energy wisps emanating from the void. Deep indigo and black colour palette."
        ),
    },
    2: {
        "name": "Root",
        "prompt": (
            f"{STYLE} "
            "Central symbol: an ancient sacred tree with deep roots spreading below and bare twisted branches above, "
            "rendered in warm amber and brown tones. The tree glows with inner golden light against the darkness. "
            "Roots form an intricate symmetrical pattern. Earth tones with golden highlights."
        ),
    },
    3: {
        "name": "Wave",
        "prompt": (
            f"{STYLE} "
            "Central symbol: three powerful ocean waves stacked vertically, rendered in deep blue and silver, "
            "with white foam crests that catch golden light. Japanese great wave style meets dark fantasy. "
            "Deep ocean blue and teal colour palette with gold accents."
        ),
    },
    4: {
        "name": "Flame",
        "prompt": (
            f"{STYLE} "
            "Central symbol: a majestic stylized flame rising upward, "
            "rendered in deep reds, oranges, and gold. The fire has an elegant ceremonial quality, "
            "like a sacred eternal flame on a dark altar. Embers float upward into darkness. "
            "Deep red and orange colour palette with bright gold core."
        ),
    },
    5: {
        "name": "Eye",
        "prompt": (
            f"{STYLE} "
            "Central symbol: a single mystical all-seeing eye, almond-shaped with a detailed iris, "
            "rendered in teal and emerald green with gold accents. "
            "The eye glows with inner knowledge and ancient wisdom. "
            "Reminiscent of the Eye of Providence or Egyptian mysticism. Teal and gold palette."
        ),
    },
    6: {
        "name": "Mask",
        "prompt": (
            f"{STYLE} "
            "Central symbol: an elegant Venetian masquerade mask floating in darkness, "
            "rendered in deep purple and violet with gold ornamental details. "
            "The mask has hollow dark eye holes and an enigmatic expression. "
            "Mysterious and theatrical. Purple and violet colour palette with gold trim."
        ),
    },
    7: {
        "name": "Key",
        "prompt": (
            f"{STYLE} "
            "Central symbol: an ornate antique skeleton key, vertical orientation, "
            "rendered in polished gold and warm amber tones. The key has an elaborate decorative bow "
            "with intricate metalwork patterns. It glows warmly against the dark background. "
            "Rich gold and amber colour palette."
        ),
    },
    8: {
        "name": "Star",
        "prompt": (
            f"{STYLE} "
            "Central symbol: a radiant eight-pointed star emanating brilliant light, "
            "rendered in magenta, pink, and silver with bright white core. "
            "The star pulses with celestial energy, rays piercing the surrounding darkness. "
            "Cosmic and powerful. Magenta and silver colour palette with bright white highlights."
        ),
    },
    9: {
        "name": "Crown",
        "prompt": (
            f"{STYLE} "
            "Central symbol: a majestic royal crown with five points, "
            "rendered in rich gold and warm amber. Jewels and ornamental details catch the light. "
            "The crown floats in darkness surrounded by a subtle golden aura, "
            "radiating supreme authority and power. Rich gold colour palette."
        ),
    },
}


def generate_image(prompt, aspect_ratio="3:4"):
    """Submit a generation request, return status_url or image_url."""
    body = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "num_results": 1,
    }
    resp = requests.post(f"{BASE_URL}/v2/image/generate", headers=HEADERS, json=body)
    resp.raise_for_status()
    data = resp.json()
    # Check if it completed synchronously
    if "result" in data and "image_url" in data.get("result", {}):
        return ("done", data["result"]["image_url"])
    return ("poll", data["status_url"])


def poll_status(status_url, timeout=180):
    """Poll until COMPLETED or FAILED."""
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
    """Download image from URL to local file."""
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)


def main():
    print("Generating 9 dark mystical card designs via Bria AI...\n")

    for pip, info in SIGNS.items():
        name = info["name"]
        prompt = info["prompt"]
        filename = f"dark_{pip:02d}_{name.lower()}.png"
        filepath = os.path.join(OUT_DIR, filename)

        print(f"  [{pip}/9] {name}... ", end="", flush=True)

        try:
            result_type, result = generate_image(prompt)
            if result_type == "poll":
                image_url = poll_status(result)
            else:
                image_url = result

            download_image(image_url, filepath)
            print(f"done -> {filename}")

        except Exception as e:
            print(f"FAILED: {e}")

    print("\nDone! Dark mystical card designs saved.")


if __name__ == "__main__":
    main()
