import json
from collections import defaultdict
from engine.intent_engine import evaluate_intent

def compute_trending(intents):
    score = defaultdict(int)

    for intent in intents:
        result = evaluate_intent(intent)

        if result["decision"] == "ALLOW":
            target = intent.get("target_user")
            score[target] += 1

    return sorted(score.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    with open("intents.json") as f:
        intents = json.load(f)

    trending = compute_trending(intents)
    print(json.dumps(trending, indent=2))
