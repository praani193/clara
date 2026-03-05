import json
import os

OUTPUT_PATH = "../outputs/accounts/"

def build_prompt(company):

    prompt = f"""
You are Clara, the AI answering assistant for {company}.

BUSINESS HOURS FLOW
1. Greet the caller politely.
2. Ask the reason for the call.
3. Collect caller name and phone number.
4. Determine if the request is emergency or non-emergency.
5. Transfer call if necessary.
6. If transfer fails apologize and take a message.
7. Ask if caller needs anything else.
8. Close the call politely.

AFTER HOURS FLOW
1. Greet the caller.
2. Ask the purpose of the call.
3. Determine if it is an emergency.
4. If emergency collect:
   - name
   - phone
   - address
5. Attempt call transfer.
6. If transfer fails apologize and assure follow-up.
7. If non-emergency collect message.
8. Ask if caller needs anything else.
9. Close politely.
"""

    return prompt


def generate_agents():

    accounts = os.listdir(OUTPUT_PATH)

    for acc in accounts:

        memo_path = OUTPUT_PATH + acc + "/v1/memo.json"

        if os.path.exists(memo_path):

            with open(memo_path) as f:
                memo = json.load(f)

            agent = {
                "agent_name": f"{memo['company_name']} AI Receptionist",
                "version": "v1",
                "voice_style": "professional",
                "system_prompt": build_prompt(memo["company_name"]),
                "key_variables": {
                    "business_hours": memo["business_hours"],
                    "services": memo["services_supported"]
                },
                "call_transfer_protocol": "Transfer to dispatcher",
                "fallback_protocol": "If transfer fails collect message"
            }

            agent_path = OUTPUT_PATH + acc + "/v1/agent_spec.json"

            with open(agent_path, "w") as out:
                json.dump(agent, out, indent=4)

            print("Agent spec created for", acc)


if __name__ == "__main__":
    generate_agents()