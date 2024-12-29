from products import Product
from store import Store

def display_menu():
    """
    Displays the menu.
    """
    print("\tStore Menu")
    print("\t----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store):
    """Displays the available products in the store."""
    products = store.get_all_products()
    if products:
        print("------")
        for i, product in enumerate(products):
            print(f"{i+1}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
        print("------")
    else:
        print("\nThere is currently no products in the store.")


def show_total_quantity(store):
    """Displays the total quantity of items in the store."""
    total_quantity = store.get_total_quantity()
    print(f"Total of {total_quantity} items in the store.")


def make_order(store):
    """Process user's order."""
    products = store.get_all_products()
    if products:
        list_products(store) # Display available products

        shopping_list = []
        while True:
            try:
                product_choice = int(input("Which product # do you want? Enter 0 to finish the order."))
                if product_choice == 0:
                    break

                if 0 < product_choice < len(products):
                    quantity = int(input("What amount do you want? "))
                    shopping_list.append((products[product_choice - 1], quantity))
                    print("Product added to the shopping list.")
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if shopping_list:
            try:
                order_price = store.order(shopping_list)
                print(f"Order made! Total payment: ${order_price}")
            except ValueError as e:
                print(f"********\nError: {e}")
        else:
            print("No products selected in this order.")
    else:
        print("There are currently no products in stock.")


def start(store):
    """Manages the user interaction loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("\nThank you for shopping at Best Buy! See you again soon.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


def main():
    """Main function to run the store application."""
    # Setup initial inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    # Start the user interaction loop
    start(best_buy)


if __name__ == "__main__":
    main()



