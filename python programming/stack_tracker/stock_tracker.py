# Step 1: Define fixed stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 330
}

# Step 2: Take user input for stocks and quantity
portfolio = {}

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter number of shares for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Sorry, we don’t have data for that stock.")

# Step 3: Calculate and display the investment summary
total_investment = 0
print("\n📊 Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment: ${total_investment}")

# Step 4: Save to file if the user wants
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter file name (like summary.txt or portfolio.csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock},{qty},{price},{investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print(f"✅ File saved as {filename}")
