print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = []

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append((stock, quantity, investment))

    print(f"✅ Added {stock} | Investment: ₹{investment}")

print("\n==============================")
print("PORTFOLIO SUMMARY")
print("==============================")

for item in portfolio:
    print(f"Stock: {item[0]} | Quantity: {item[1]} | Value: ₹{item[2]}")

print("\nTotal Investment Value: ₹", total_investment)

save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("STOCK PORTFOLIO SUMMARY\n\n")

    for item in portfolio:
        file.write(f"{item[0]} - Qty: {item[1]} - Value: ₹{item[2]}\n")

    file.write(f"\nTotal Investment Value: ₹{total_investment}")
    file.close()

    print("📁 Portfolio saved to portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")
