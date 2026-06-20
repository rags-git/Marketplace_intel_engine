import json
import random

def fetch_live_demand_signals():
    # This generates a fresh demand multiplier every time the function is called
    data = {
        "demand_multiplier": round(random.uniform(1.0, 2.0), 2),
        "region": "Market-Alpha"
    }
    
    # Ensure this saves to the data folder in your project root
    with open("data/market_demand.json", "w") as f:
        json.dump(data, f)
    return data