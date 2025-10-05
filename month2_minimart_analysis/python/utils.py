# Utility functions for data conversion and filtering
def flag_large_order(order, threshold=10):
    """
    Adds a flag 'large_order' if total price exceeds threshold
    """
    total = order["quantity"] * order["price"]
    if total > threshold:
        order["large_order"] = True
    else:
        order["large_order"] = False
    return order

def convert_currency(report, rate=1.0):
    """
    Converts all revenue values per customer by a conversion rate
    """
    for customer in report["revenue_per_customer"]:
        report["revenue_per_customer"][customer] *= rate
    return report
