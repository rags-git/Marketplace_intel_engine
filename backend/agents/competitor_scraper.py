import json
import random

def scrape_live_competitor_pricing():
    data = []
    # This generates fresh mock data every time the function is called
    for i in range(5):
        price = round(random.uniform(50, 150), 2)
        data.append({"equipment_id": i, "competitor_price": price})
    
    # Ensure this saves to the data folder in your project root
    with open("data/competitor_intel.json", "w") as f:
        json.dump(data, f)
    return data