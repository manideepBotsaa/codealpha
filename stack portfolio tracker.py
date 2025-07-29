# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 290
}

total_value = 0
portfolio = {}

print("Enter your stock portfolio (type 'done' to finish):")
while True:
    stock = input("Stock symbol (AAPL/TSLA/GOOGL/AMZN/MSFT): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in list. Try again.")
        continue
    quantity = int(input(f"Quantity of {stock}: "))
    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

print("\n📊 Investment Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}")
print(f"\n💰 Total Investment Value: ${total_value}")

# Optional file saving
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        f.write(f"\nTotal Investment: ${total_value}")
    print("Saved to portfolio_summary.txt")
