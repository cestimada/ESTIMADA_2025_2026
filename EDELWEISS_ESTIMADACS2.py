names = []
prices = []

def add_product():
    print(" Add Product ")
    name = input("Enter product name: ")
    if name in names:
        print("Product already exists!")
    else:
        try:
            price = float(input("Enter price: ₱"))
            names.append(name)
            prices.append(price)
            print("Product added successfully!")
        except:
            print("Invalid price!")

def show_products():
    print(" Product List ")
    if not names:
        print("No products yet.")
    else:
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ₱{prices[i]:.2f}")

def search_product():
    print(" Search Product ")
    name = input("Enter product name: ")
    if name in names:
        i = names.index(name)
        print(f"{names[i]} costs ₱{prices[i]:.2f}")
    else:
        print("Product not found.")

def update_price():
    print(" Update Price ")
    name = input("Enter product name: ")
    if name in names:
        try:
            new_price = float(input("Enter new price: ₱"))
            i = names.index(name)
            prices[i] = new_price
            print("Price updated successfully!")
        except:
            print("Invalid price!")
    else:
        print("Product not found.")

def delete_product():
    print(" Delete Product ")
    name = input("Enter product name: ")
    if name in names:
        i = names.index(name)
        prices.remove(prices[i])
        names.remove(name)
        print("Product deleted!")
    else:
        print("Product not found.")

def total_price():
    print(" Total Inventory Value ")
    total = sum(prices)
    print(f"Total Value: ₱{total:.2f}")

# Main menu
while True:
    print(" PRODUCT MENU ")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Price")
    print("5. Delete Product")
    print("6. Total Value")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_price()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        total_price()
    elif choice == "7":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice. Try again.")
