import json
import os

OUTPUT_PATH = "../outputs/accounts/"

def update_account(account_id, updates):

    v1_path = OUTPUT_PATH + account_id + "/v1/memo.json"

    with open(v1_path) as f:
        memo = json.load(f)

    for key, value in updates.items():
        memo[key] = value

    v2_folder = OUTPUT_PATH + account_id + "/v2/"
    os.makedirs(v2_folder, exist_ok=True)

    with open(v2_folder + "memo.json", "w") as f:
        json.dump(memo, f, indent=4)

    changes = {
        "updated_fields": list(updates.keys())
    }

    with open(v2_folder + "changes.json", "w") as f:
        json.dump(changes, f, indent=4)

    print("Account updated to v2")


if __name__ == "__main__":

    update_account(
        "ACCOUNT_ID_HERE",
        {
            "business_hours": "Mon-Fri 8AM-5PM PST",
            "emergency_definition": ["Power outage", "Burning smell"],
            "call_transfer_rules": "Transfer within 60 seconds"
        }
    )