import requests
from requests.auth import HTTPBasicAuth

subdomain = "z3nccaballero1757082303"
admin_email = "cesaraugusto.caballero@zendesk.com/token"  # replace with your sandbox admin email
api_token = "yqsMWLXCeeYlJnkv2oXAwB3QX2TaIeSfSv1PaBK7"          # replace with your sandbox API token

# Coen Brothers movies
coen_movies = ["Fargo", "The Big Lebowski", "No Country for Old Men", "O Brother, Where Art Thou?", "Burn After Reading"]

for i, movie in enumerate(coen_movies, start=1):
    payload = {
        "group": {
            "name": movie
        }
    }

    response = requests.post(
        f"https://{subdomain}.zendesk.com/api/v2/groups.json",
        json=payload,
        auth=HTTPBasicAuth(f"{admin_email}/token", api_token),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print(f"{i}: Created group '{movie}'")
    else:
        print(f"{i}: Failed to create '{movie}' - Status {response.status_code}: {response.text}")
