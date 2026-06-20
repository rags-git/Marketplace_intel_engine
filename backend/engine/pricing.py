import json
import pandas as pd
import numpy as np

def calculate_dynamic_pricing():
    print("Initializing Mathematical Optimization Engine...")

    # 1. Ingest Data from Phase 2
    try:
        with open("data/competitor_intel.json", "r") as f:
            competitor_data = json.load(f)
        with open("data/market_demand.json", "r") as f:
            demand_data = json.load(f)
    except FileNotFoundError:
        print("Error: Missing data files. Run Agents A and B first.")
        return

    # 2. Process Competitor Data using Pandas
    df = pd.DataFrame(competitor_data)
    avg_competitor_price = df['competitor_price'].mean()
    supply_density = len(df) # Number of competitors found
    print(f"Market Analysis: Found {supply_density} competitors with an average price of ${avg_competitor_price:.2f}")

    # 3. Process Demand Data
    demand_index = demand_data.get("demand_multiplier", 1.0)
    print(f"Market Demand Index: {demand_index}x")

    # 4. Mathematical Optimization Formula
    base_fee = 25.00
    alpha = 15.00
    beta = 5.00

    # Processing Fee = Base Fee + (Alpha * Demand Index) - (Beta * Competitor Supply Density)
    calculated_fee = base_fee + (alpha * demand_index) - (beta * supply_density)

    # Use NumPy to ensure the fee never drops below a minimum hard floor of $10.00
    optimal_fee = float(np.maximum(calculated_fee, 10.00))
    
    print("\n--- OPTIMIZATION RESULTS ---")
    print(f"Optimal Transaction Processing Fee: ${optimal_fee:.2f}")

    # 5. Financial Unit Economics & Breakeven Forecast
    target_founder_salary = 120000
    monthly_operational_burn = 4000 + (target_founder_salary / 12)
    estimated_monthly_transactions = 1200
    
    projected_monthly_revenue = estimated_monthly_transactions * optimal_fee
    net_profit = projected_monthly_revenue - monthly_operational_burn

    print("\n--- UNIT ECONOMICS FORECAST ---")
    print(f"Monthly Operational Burn: ${monthly_operational_burn:.2f}")
    print(f"Projected Monthly Revenue: ${projected_monthly_revenue:.2f}")
    
    if net_profit > 0:
        print(f"Status: PROFITABLE (Surplus of ${net_profit:.2f}/month)")
    else:
        print(f"Status: OPERATING AT A LOSS (Deficit of ${abs(net_profit):.2f}/month)")

if __name__ == "__main__":
    calculate_dynamic_pricing()