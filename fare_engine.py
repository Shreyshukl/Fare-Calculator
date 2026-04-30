# fare_engine.py
# -------------------------------------------------------
# Purpose : Core fare calculation logic for CityCab
# Author  : Shrey Shukla
# Year    : 2026
# -------------------------------------------------------

# --- Vehicle Rates (per km in ₹) ---
VEHICLE_RATES = {
    "Motorcycle": 6,
    "Auto":       9,
    "Economy":    10,
    "Premium":    18,
    "SUV":        25
}

# --- Aliases ---
# Only for genuinely different words that mean the same vehicle
# Everything else is handled by case-insensitive matching
VEHICLE_ALIASES = {
    "bike":       "Motorcycle",
    "motorbike":  "Motorcycle"
}

SURGE_MULTIPLIER = 1.5
SURGE_START_HOUR = 17
SURGE_END_HOUR   = 20


def resolve_vehicle_type(user_input: str):
    """
    Resolve user input to an official vehicle type.
    - Strips spaces and converts to lowercase first
    - Then checks aliases (bike, motorbike → Motorcycle)
    - Then checks official names case-insensitively

    Args:
        user_input (str): Raw input from user

    Returns:
        str or None: Official vehicle name if found, else None
    """
    # Clean the input — remove spaces, make lowercase
    # This handles SUV, suv, Suv, sUv all the same way
    cleaned = user_input.strip().lower()

    # Step 1: Check aliases first (bike → Motorcycle etc.)
    if cleaned in VEHICLE_ALIASES:
        return VEHICLE_ALIASES[cleaned]

    # Step 2: Match against official names case-insensitively
    # e.g. "suv" will match "SUV", "economy" will match "Economy"
    for official_name in VEHICLE_RATES:
        if cleaned == official_name.lower():
            return official_name

    # Step 3: Nothing matched
    return None


def is_surge_hour(hour: int) -> bool:
    """
    Check if the given hour falls in peak/surge pricing window.

    Args:
        hour (int): Hour of the day in 24-hour format (0-23)

    Returns:
        bool: True if surge pricing applies, False otherwise
    """
    return SURGE_START_HOUR <= hour <= SURGE_END_HOUR


def calculate_fare(km: float, vehicle_type: str, hour: int) -> dict:
    """
    Calculate the total ride fare based on distance, vehicle, and time.

    Args:
        km           (float): Distance in kilometres
        vehicle_type  (str) : Official vehicle type
        hour          (int) : Hour of booking in 24-hour format (0-23)

    Returns:
        dict: Full fare breakdown
    """
    rate_per_km  = VEHICLE_RATES[vehicle_type]
    base_fare    = km * rate_per_km

    surge_applied = is_surge_hour(hour)
    multiplier    = SURGE_MULTIPLIER if surge_applied else 1.0
    final_fare    = base_fare * multiplier

    return {
        "vehicle_type":  vehicle_type,
        "km":            km,
        "rate_per_km":   rate_per_km,
        "base_fare":     base_fare,
        "surge_applied": surge_applied,
        "multiplier":    multiplier,
        "final_fare":    final_fare
    }
