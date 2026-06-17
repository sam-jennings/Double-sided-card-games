"""Generate 9 card symbol icons via Bria AI image generation.

Uses the Nine Signs set at 3:4 aspect ratio (card portrait).
Polls async results and downloads the final images.
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

# Each prompt is crafted for a bold, high-contrast card game symbol icon
SIGNS = {
    1: {
        "name": "Void",
        "prompt": (
            "A bold symbolic card game icon representing THE VOID: "
            "a dark indigo circular portal or ring with an empty center, "
            "suggesting cosmic nothingness and absence. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean silhouette style. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    2: {
        "name": "Root",
        "prompt": (
            "A bold symbolic card game icon representing THE ROOT: "
            "a deep brown ancient tree with spreading roots below and bare branches above, "
            "forming a symmetrical emblem of grounding and connection. "
            "Rendered as a striking high-contrast silhouette centered on a warm cream background. "
            "Mystical, archetypal, clean emblem style. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    3: {
        "name": "Wave",
        "prompt": (
            "A bold symbolic card game icon representing THE WAVE: "
            "three flowing ocean blue wave curves stacked vertically, "
            "suggesting water, flow, and movement. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean graphic style like a Japanese wave motif. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    4: {
        "name": "Flame",
        "prompt": (
            "A bold symbolic card game icon representing THE FLAME: "
            "a stylized red and orange fire with a teardrop shape rising upward, "
            "suggesting energy, destruction, and passion. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean silhouette style. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    5: {
        "name": "Eye",
        "prompt": (
            "A bold symbolic card game icon representing THE EYE: "
            "a single mystical all-seeing eye in teal green, almond-shaped with a detailed iris, "
            "suggesting knowledge, sight, and surveillance. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean graphic style like an Egyptian eye of Horus. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    6: {
        "name": "Mask",
        "prompt": (
            "A bold symbolic card game icon representing THE MASK: "
            "a violet theatrical mask with hollow eye holes, "
            "suggesting disguise, deception, and hidden identity. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean silhouette style like a venetian masquerade mask. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    7: {
        "name": "Key",
        "prompt": (
            "A bold symbolic card game icon representing THE KEY: "
            "an ornate golden skeleton key with a circular bow and decorative teeth, "
            "suggesting access, secrets, and unlocking. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean silhouette style. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    8: {
        "name": "Star",
        "prompt": (
            "A bold symbolic card game icon representing THE STAR: "
            "a radiant magenta eight-pointed star with sharp rays emanating outward, "
            "suggesting the wild, the special, and celestial power. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean graphic style. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
    9: {
        "name": "Crown",
        "prompt": (
            "A bold symbolic card game icon representing THE CROWN: "
            "a majestic golden crown with five points and jewels, "
            "suggesting royalty, the apex, and supreme authority. "
            "Rendered as a striking high-contrast emblem centered on a warm cream background. "
            "Mystical, archetypal, clean silhouette style. "
            "Suitable for a tabletop card game symbol. No text, no words, no letters."
        ),
    },
}


def generate_image(prompt, aspect_ratio="3:4"):
    """Submit a generation request, return status_url."""
    body = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "num_results": 1,
    }
    resp = requests.post(f"{BASE_URL}/v2/image/generate", headers=HEADERS, json=body)
    resp.raise_for_status()
    data = resp.json()
    return data.get("status_url") or data.get("result", {}).get("image_url")


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
    print("Generating 9 card symbol icons via Bria AI...\n")

    for pip, info in SIGNS.items():
        name = info["name"]
        prompt = info["prompt"]
        filename = f"bria_{pip:02d}_{name.lower()}.png"
        filepath = os.path.join(OUT_DIR, filename)

        print(f"  [{pip}/9] {name}... ", end="", flush=True)

        try:
            result = generate_image(prompt)

            # If result is a URL directly (sync completed), use it
            if result and result.startswith("http") and "status" not in result:
                image_url = result
            else:
                # It's a status_url, poll it
                image_url = poll_status(result)

            download_image(image_url, filepath)
            print(f"✓ {filename}")

        except Exception as e:
            print(f"✗ FAILED: {e}")

    print("\nDone! Check the Designs/ folder.")


if __name__ == "__main__":
    main()
