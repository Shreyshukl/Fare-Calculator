# CityCab Fare Calculator

## Overview
CityCab Fare Calculator is a command-line Python application for computing ride fares based on distance, vehicle category, and time of booking. The system incorporates surge pricing during peak hours and ensures reliable operation through structured input validation.

---

## Key Features
- Configurable vehicle categories with per-kilometer pricing  
- Distance-based fare computation  
- Peak-hour surge pricing mechanism  
- Robust input validation and error handling  
- Structured fare breakdown and receipt generation  
- Continuous execution support for multiple fare calculations  

---

## Architecture
The application follows a modular design:

- **main.py** — Application entry point and workflow orchestration  
- **fare_engine.py** — Core business logic for fare computation  
- **validator.py** — Input validation and normalization  
- **receipt.py** — Output formatting and presentation  

---

## Pricing Model

### Vehicle Rates
| Category     | Rate (₹/km) |
|--------------|------------|
| Motorcycle   | 6          |
| Auto         | 9          |
| Economy      | 10         |
| Premium      | 18         |
| SUV          | 25         |

### Surge Pricing
- Time Window: 17:00 – 20:00  
- Multiplier: 1.5×  

---

## Execution

### Prerequisites
- Python 3.x

### Run the Application
```bash
python main.py
```

---

## Input Specifications
- **Distance**: Positive numeric value  
- **Vehicle Type**: Case-insensitive, supports alias resolution  
- **Hour**: Integer value in range 0–23  

---

## Output
The application generates a formatted receipt including:
- Vehicle type  
- Distance and rate  
- Base fare  
- Surge status  
- Final payable amount
  
<img width="598" height="764" alt="WhatsApp Image 2026-04-30 at 23 28 13" src="https://github.com/user-attachments/assets/25628ece-1f19-432c-bfb5-c9fd7eafd18e" />

---

## Extensibility
The modular structure allows easy extension for:
- Additional vehicle categories  
- Dynamic pricing strategies  
- API or GUI integration  
- Persistent data storage  

---


