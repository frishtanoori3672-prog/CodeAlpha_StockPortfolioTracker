# CodeAlpha Task 2 - Stock Portfolio Tracker

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160,
    "AMZN": 190
}

print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

total_investment = 0
portfolio = []

print("\nEnter the stocks you want to add.")
print("Type 'done' when you are finished.")

while True:

    stock = input("\nEnter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    price = stock_prices[stock]

    investment_value = price * quantity

    total_investment += investment_value

    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "value": investment_value
    })

    print(f"{stock} added successfully!")
    print(f"Investment value: ${investment_value:,.2f}")


print("\n" + "=" * 45)
print("          PORTFOLIO SUMMARY")
print("=" * 45)

if len(portfolio) == 0:

    print("No stocks were added.")

else:

    for item in portfolio:
        print(
            f"{item['stock']} | "
            f"Quantity: {item['quantity']} | "
            f"Price: ${item['price']} | "
            f"Value: ${item['value']:,.2f}"
        )

    print("-" * 45)
    print(f"Total Investment: ${total_investment:,.2f}")


# Save the result in a text file
with open("portfolio_result.txt", "w") as file:

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=" * 40 + "\n\n")

    if len(portfolio) == 0:

        file.write("No stocks were added.\n")

    else:

        for item in portfolio:
            file.write(
                f"{item['stock']} | "
                f"Quantity: {item['quantity']} | "
                f"Price: ${item['price']} | "
                f"Value: ${item['value']:,.2f}\n"
            )

        file.write("\n")
        file.write(
            f"Total Investment: ${total_investment:,.2f}\n"
        )


print("\nYour result has been saved to portfolio_result.txt")
print("Thank you for using Stock Portfolio Tracker!")