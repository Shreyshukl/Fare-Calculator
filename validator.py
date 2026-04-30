# validator.py
# -------------------------------------------------------
# Purpose : Input validation for CityCab FareCalc
# Author  : Shrey Shukla
# Year    : 2026
# -------------------------------------------------------

from fare_engine import VEHICLE_RATES, resolve_vehicle_type


def get_valid_distance() -> float:
    """
    Prompt the user to enter a valid distance in km.
    Keeps asking until a positive number is entered.

    Returns:
        float: Valid distance entered by the user
    """
    while True:
        try:
            km = float(input("Enter distance (in km): "))
            if km <= 0:
                print("  ⚠  Distance must be greater than 0. Try again.\n")
            else:
                return km
        except ValueError:
            print("  ⚠  Invalid input. Please enter a number (e.g. 5.2).\n")


def get_valid_vehicle() -> str:
    """
    Display available vehicle options and prompt user to choose one.
    Accepts official names, aliases, and is fully case-insensitive.

    Returns:
        str: Official vehicle type resolved from user input
    """
    print("\nAvailable vehicle types:")
    for vehicle, rate in VEHICLE_RATES.items():
        print(f"{vehicle:<12} →  ₹{rate}/km")

    while True:
        choice = input("Enter vehicle type: ")
        resolved = resolve_vehicle_type(choice)

        if resolved:
            print(f"  ✅ Got it! Booking a {resolved} for you.\n")
            return resolved
        else:
            print(f"  ⚠  '{choice}' is not recognized.")
            print("  Try: Motorcycle, Auto, Economy, Premium, SUV")
            print("  Or aliases like: bike, car, sedan, eco, rickshaw\n")


def get_valid_hour() -> int:
    """
    Prompt the user to enter a valid hour in 24-hour format.
    Keeps asking until a value between 0 and 23 is entered.

    Returns:
        int: Valid hour entered by the user
    """
    while True:
        try:
            hour = int(input("Enter current hour (0-23): "))
            if 0 <= hour <= 23:
                return hour
            else:
                print("  ⚠  Hour must be between 0 and 23. Try again.\n")
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number (e.g. 17).\n")