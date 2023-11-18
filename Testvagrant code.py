Import-Module PSReadLine
# Product details in the basket
products_in_basket = [
    {"name": "leather wallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
    {"name": "umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
    {"name": "cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
    {"name": "honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2},
]

# Function to calculate GST amount for a product
def calculate_gst_amount(unit_price, gst_percentage, quantity):
    gst_amount = (unit_price * gst_percentage / 100) * quantity
    return gst_amount

# 1. Identify the product for which we paid the maximum GST amount
max_gst_product = max(products_in_basket, key=lambda x: calculate_gst_amount(x["unit_price"], x["gst_percentage"], x["quantity"]))
print("Product with the maximum GST amount:", max_gst_product["name"])

# 2. Calculate the total amount to be paid to the shopkeeper
total_amount = sum([(p["unit_price"] * p["quantity"]) + calculate_gst_amount(p["unit_price"], p["gst_percentage"], p["quantity"]) for p in products_in_basket])
print("Total amount to be paid to the shopkeeper:", total_amount)