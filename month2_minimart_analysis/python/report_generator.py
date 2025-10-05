# Code to generate dictionary summary reports
from utils import flag_large_order

# Sample orders
orders = [
    {"customer": "Alice", "product": "Coke", "quantity": 3, "price": 2.5},
    {"customer": "Bob", "product": "Bread", "quantity": 2, "price": 3.0},
    {"customer": "Alice", "product": "Milk", "quantity": 1, "price": 2.0},
    {"customer": "Charlie", "product": "Water", "quantity": 5, "price": 1.0},
    {"customer": "Diana", "product": "Cheese", "quantity": 2, "price": 4.5},
]

def generate_report():
    report = {
        "total_products_sold": 0,
        "most_popular_product": None,
        "revenue_per_customer": {}
    }
    product_count = {}

    for order in orders:
        # Total products sold
        report["total_products_sold"] += order["quantity"]
        
        # Count per product for popularity
        product_count[order["product"]] = product_count.get(order["product"], 0) + order["quantity"]
        
        # Revenue per customer
        report["revenue_per_customer"][order["customer"]] = \
            report["revenue_per_customer"].get(order["customer"], 0) + order["quantity"] * order["price"]
        
        # Optional: flag large orders
        flag_large_order(order)

    # Most popular product
    report["most_popular_product"] = max(product_count, key=product_count.get)
    
    return report
