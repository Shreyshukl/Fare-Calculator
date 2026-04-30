# receipt.py
# -------------------------------------------------------
# Purpose : Format and display the CityCab price receipt
# Author  : Shrey Shukla
# Year    : 2026
# -------------------------------------------------------

from datetime import datetime


def print_receipt(fare_details: dict) -> None:
    """
    Print a formatted price receipt to the console.

    Args:
        fare_details (dict): Fare breakdown returned by calculate_fare()
    """
    now = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    border = "=" * 40

    print(f"\n{border}")
    print("CITYCAB — PRICE RECEIPT")
    print(border)
    print(f"  Date & Time     : {now}")
    print(f"  Vehicle Type    : {fare_details['vehicle_type']}")
    print(f"  Distance        : {fare_details['km']} km")
    print(f"  Rate            : ₹{fare_details['rate_per_km']}/km")
    print(f"  Base Fare       : ₹{fare_details['base_fare']:.2f}")
    print("-" * 40)

    if fare_details["surge_applied"]:
        print(f"  Surge Pricing : {fare_details['multiplier']}x  (Peak Hours)")
    else:
        print("No Surge Pricing (Off-Peak)")

    print("-" * 40)
    print(f"  TOTAL FARE      : ₹{fare_details['final_fare']:.2f}")
    print(f"{border}\n")
