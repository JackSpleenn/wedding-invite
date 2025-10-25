import requests
from requests.auth import HTTPBasicAuth
import random

# 🔹 Sandbox info
subdomain = "z3nccaballero1757082303"

# 🔹 Your admin credentials (replace with your sandbox admin email and API token)
admin_email = "cesaraugusto.caballero@zendesk.com/token"
api_token = "yqsMWLXCeeYlJnkv2oXAwB3QX2TaIeSfSv1PaBK7"

# 🔹 List of comic book character names
comic_names = [
    "Spider-Man", "Batman", "Wonder Woman", "Iron Man", "Black Panther",
    "Doctor Strange", "Flash", "Aquaman", "Green Lantern", "Captain Marvel",
    "Harley Quinn", "Deadpool", "Joker", "Magneto", "Thanos",
    "Loki", "Daredevil", "Green Arrow", "Cyclops", "Storm"
]

# 🔹 Maximum agents your sandbox allows
MAX_AGENTS = 5  # adjust if your sandbox allows more

for i in range(MAX_AGENTS):
    name = random.choice(comic_names) + f" {i+1}"
    email = f"user{i+1}@example.com"  # must be unique

    payload = {
        "user": {
            "name": name,
            "email": email,
            "role": "agent",
            "custom_role": 39349043116557  # built-in Light Agent
        }
    }

    response = requests.post(
        f"https://{subdomain}.zendesk.com/api/v2/users.json",
        json=payload,
        auth=HTTPBasicAuth(f"{admin_email}/token", api_token),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print(f"{i+1}: Created Light Agent '{name}' with email '{email}'")
    else:
        print(f"{i+1}: Failed to create '{name}' - Status {response.status_code}: {response.text}")
