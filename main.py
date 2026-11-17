import argparse
import time

from crypto import get_crypto_prices
from database import create_table, save_price, get_history


def display_prices():

    print("\n========== CRYPTOCURRENCY PRICE TRACKER ==========\n")

    data = get_crypto_prices()

    if not data:
        print("Unable to fetch cryptocurrency prices.")
        return

    for coin in data:

        name = coin["name"]
        symbol = coin["symbol"].upper()
        price = coin["current_price"]
        market_cap = coin["market_cap"]
        volume = coin["total_volume"]

        print("------------------------------------------")
        print("Coin Name :", name)
        print("Symbol    :", symbol)
        print("Price     : $", price)
        print("Market Cap: $", market_cap)
        print("Volume    : $", volume)

        save_price(
            name,
            symbol,
            price or 0,
            market_cap or 0,
            volume or 0
        )

    print("\nPrices updated successfully!")


def show_history():

    print("\n========== PRICE HISTORY ==========\n")

    records = get_history()

    if not records:
        print("No price history available.")
        return

    for record in records:

        print(
            "Coin:", record[0],
            "| Symbol:", record[1],
            "| Price: $", record[2],
            "| Time:", record[3]
        )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--headless",
        action="store_true"
    )

    args = parser.parse_args()

    create_table()

    print("INFO: Cryptocurrency Price Tracker Started!")

    while True:

        display_prices()

        if args.headless:
            break

        print("\n1. Refresh Prices")
        print("2. View Price History")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nRefreshing prices...")
            time.sleep(2)

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Thank you for using Cryptocurrency Price Tracker!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()