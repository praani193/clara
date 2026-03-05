import json
import os
import uuid

DATASET_PATH = "../dataset/demo/"
OUTPUT_PATH = "../outputs/accounts/"

def extract_basic_info(transcript):

    memo = {
        "account_id": str(uuid.uuid4())[:8],
        "company_name": None,
        "business_hours": None,
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": None,
        "non_emergency_routing_rules": None,
        "call_transfer_rules": None,
        "integration_constraints": [],
        "after_hours_flow_summary": None,
        "office_hours_flow_summary": None,
        "questions_or_unknowns": [],
        "notes": ""
    }

    text = transcript.lower()

    if "electric" in text:
        memo["services_supported"].append("Electrical services")

    if "ev charger" in text:
        memo["services_supported"].append("EV charger installation")

    if "hot tub" in text:
        memo["services_supported"].append("Hot tub electrical hookup")

    if "jobber" in text:
        memo["integration_constraints"].append("Uses Jobber CRM")

    if "emergency" not in text:
        memo["questions_or_unknowns"].append("Emergency definition not mentioned")

    if "hours" not in text:
        memo["questions_or_unknowns"].append("Business hours not specified")

    return memo


def process_transcripts():

    for file in os.listdir(DATASET_PATH):

        if file.endswith(".txt"):

            with open(DATASET_PATH + file, "r", encoding="utf-8") as f:
                transcript = f.read()

            memo = extract_basic_info(transcript)

            account_folder = OUTPUT_PATH + memo["account_id"] + "/v1/"
            os.makedirs(account_folder, exist_ok=True)

            with open(account_folder + "memo.json", "w") as out:
                json.dump(memo, out, indent=4)

            print("Generated memo for", memo["account_id"])


if __name__ == "__main__":
    process_transcripts()