# Entry point for the MiniMart data reporting system
from report_generator import generate_report
from utils import convert_currency

if __name__ == "__main__":
    report = generate_report()
    
    # Optional: convert revenue to another currency (example: USD → EUR)
    report = convert_currency(report, rate=0.91)
    
    import json
    print(json.dumps(report, indent=4))

