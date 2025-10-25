import requests
from requests.auth import HTTPBasicAuth

# 🔹 Sandbox info
subdomain = "z3nccaballero1757082303"
admin_email = "cesaraugusto.caballero@zendesk.com/token"  # replace with your sandbox admin email
api_token = "yqsMWLXCeeYlJnkv2oXAwB3QX2TaIeSfSv1PaBK7"          # replace with your sandbox API token

# 🔹 Ticket settings
assignee_name = "Reverse Flash"
group_name = "The Big Lebowski"

# Ticket subjects and descriptions
ticket_subjects = [
    "Issue with login",
    "Unable to reset password",
    "Bug in checkout flow",
    "Feature request: Dark mode",
    "Error 500 on dashboard",
    "Question about API",
    "Feedback on new UI"
]

# 🔹 Helper function to get user ID by name
def get_user_id_by_name(name):
    url = f"https://{subdomain}.zendesk.com/api/v2/users.json?query={name}"
    response = requests.get(url, auth=HTTPBasicAuth(f"{admin_email}/token", api_token))
    users = response.json().get("users", [])
    for user in users:
        if user["name"] == name:
            return user["id"]
    return None

# 🔹 Helper function to get group ID by name
def get_group_id_by_name(name):
    url = f"https://{subdomain}.zendesk.com/api/v2/groups.json"
    response = requests.get(url, auth=HTTPBasicAuth(f"{admin_email}/token", api_token))
    groups = response.json().get("groups", [])
    for group in groups:
        if group["name"] == name:
            return group["id"]
    return None

# 🔹 Get IDs
assignee_id = get_user_id_by_name(assignee_name)
group_id = get_group_id_by_name(group_name)

if not assignee_id:
    raise Exception(f"Assignee '{assignee_name}' not found")
if not group_id:
    raise Exception(f"Group '{group_name}' not found")

# 🔹 Create 7 tickets
for i, subject in enumerate(ticket_subjects, start=1):
    payload = {
        "ticket": {
            "subject": subject,
            "comment": {"body": f"This is ticket #{i} for testing purposes."},
            "assignee_id": assignee_id,
            "group_id": group_id
        }
    }

    response = requests.post(
        f"https://{subdomain}.zendesk.com/api/v2/tickets.json",
        json=payload,
        auth=HTTPBasicAuth(f"{admin_email}/token", api_token),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print(f"{i}: Created ticket '{subject}' assigned to {assignee_name}")
    else:
        print(f"{i}: Failed to create ticket '{subject}' - Status {response.status_code}: {response.text}")
