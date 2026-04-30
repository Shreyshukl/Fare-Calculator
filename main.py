# main.py
# -------------------------------------------------------
# Purpose : Entry point for CityCab FareCalc application
# Author  : Shrey Shukla
# Year    : 2026
# -------------------------------------------------------

from fare_engine import calculate_fare
from validator import get_valid_distance, get_valid_vehicle, get_valid_hour
from receipt import print_receipt


def main():
    """
    Main function — orchestrates the CityCab fare calculation flow.
    """
    print("\n" + "=" * 40)
    print("    🚕  Welcome to CityCab FareCalc")
    print("=" * 40)

    # Step 1: Collect inputs (validator handles all errors)
    km = get_valid_distance()
    vehicle_type = get_valid_vehicle()
    hour = get_valid_hour()

    # Step 2: Calculate fare (fare_engine does the math)
    fare_details = calculate_fare(km, vehicle_type, hour)

    # Step 3: Display receipt (receipt handles all printing)
    print_receipt(fare_details)

    # Step 4: Ask if user wants another estimate
    again = input("Calculate another fare? (yes / no): ").strip().lower()
    if again == "yes":
        main()  # Restart the program
    else:
        print("\nThank you for using CityCab! 🚕\n")


# Industry standard — this ensures main() only runs
# when YOU run this file directly, not when imported
if __name__ == "__main__":
    main()