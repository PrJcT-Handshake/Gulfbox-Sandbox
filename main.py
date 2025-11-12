import os
from data_handler import load_balance_sheet, summarize_balance
from basel_calculator import calculate_car, calculate_lcr, calculate_nsfr

def main():
    print("\n🔎 Gulfbox Sandbox — Basel III Risk Simulation\n")

    # Step 1: Load the balance sheet data
    file_path = os.path.join("data", "sample_balance.xlsx")
    df = load_balance_sheet(file_path)
    summary = summarize_balance(df)
    print("📊 Balance Sheet Summary:", summary)

    # Step 2: Compute Basel ratios
    tier1_capital = 500
    risk_weighted_assets = 4000
    hqla = 1200
    net_outflows_30d = 1000
    asf = 3500
    rsf = 3000

    ratios = {
        "CAR (%)": calculate_car(tier1_capital, risk_weighted_assets),
        "LCR (%)": calculate_lcr(hqla, net_outflows_30d),
        "NSFR (%)": calculate_nsfr(asf, rsf),
    }

    print("\n✅ Basel III Ratios:")
    for name, value in ratios.items():
        print(f"  - {name}: {value:.2f}")

if __name__ == "__main__":
    main()
