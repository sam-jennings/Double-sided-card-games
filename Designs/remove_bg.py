"""Remove backgrounds from the 9 emblems via Bria RMBG-2.0.

Uploads each local emblem, gets a transparent PNG cutout back, saves it.
Bria's remove_background needs a publicly accessible URL OR base64 image.
We pass base64 data URLs.
"""

import requests
import time
import os
import base64

API_KEY = "fd37cb947b5e42b7a192d7c504fc9762"
BASE_URL = "https://engine.prod.bria-api.com"
HEADERS = {
    "api_token": API_KEY,
    "Content-Type": "application/json",
    "User-Agent": "BriaSkills/1.3.4",
}

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

SIGNS = {1: "Void", 2: "Root", 3: "Wave", 4: "Flame", 5: "Eye",
         6: "Mask", 7: "Key", 8: "Star", 9: "Crown"}


def to_data_url(path):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/png;base64,{b64}"


def remove_background(image_data_url):
    body = {"image": image_data_url}
    resp = requests.post(f"{BASE_URL}/v2/image/edit/remove_background",
                         headers=HEADERS, json=body)
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
            raise Exception(f"Failed: {data}")
        time.sleep(3)
    raise TimeoutError("timeout")


def download_image(url, filepath):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)


def main():
    print("Removing backgrounds from 9 emblems via Bria RMBG...\n")
    for pip, name in SIGNS.items():
        src = os.path.join(OUT_DIR, f"emblem_{pip:02d}_{name.lower()}.png")
        dst = os.path.join(OUT_DIR, f"cutout_{pip:02d}_{name.lower()}.png")
        print(f"  [{pip}/9] {name}... ", end="", flush=True)
        try:
            data_url = to_data_url(src)
            result_type, result = remove_background(data_url)
            image_url = poll_status(result) if result_type == "poll" else result
            download_image(image_url, dst)
            print(f"done -> cutout_{pip:02d}_{name.lower()}.png")
        except Exception as e:
            print(f"FAILED: {e}")
    print("\nDone! Transparent cutouts saved.")


if __name__ == "__main__":
    main()
