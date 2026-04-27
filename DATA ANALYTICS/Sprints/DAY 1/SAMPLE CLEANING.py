raw_prices = ["$10.00", "$25.50", None, "$5.00", "FREE"]

clean_prices = []

for price in raw_prices:
    if price is None or price == "FREE":
        clean_prices.append(0.0)
    else:
        # Remove '$' and convert to decimal (float)
        clean_value = float(price.replace("$", ""))
        clean_prices.append(clean_value)

print(f"Cleaned Data: {clean_prices}") 
# Output: [10.0, 25.5, 0.0, 5.0, 0.0]
