from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random
import pandas as pd
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/metrics")
async def get_optimized_metrics(file: UploadFile = File(None)):
    # 1. Determine Data Source
    if file:
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))
        supply_density = len(df)
        demand_index = 1.25
        region = "CSV Upload"
    else:
        # 2. Simulate "Scraping" in-memory (No file dependencies)
        supply_density = random.randint(1, 10)
        demand_index = round(random.uniform(1.0, 2.0), 2)
        region = "Live Market"

    # 3. Core Calculation
    optimal_fee = max(25.0 + (15.0 * demand_index) - (5.0 * supply_density), 10.0)
    
    return {
        "success": True,
        "market_indicators": {"competitor_count": supply_density, "demand_index": demand_index, "region": region},
        "optimization_results": {"optimal_processing_fee": round(optimal_fee, 2)},
        "financial_forecast": {"net_profit": (1200 * optimal_fee) - 14000.0}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)