
#-----
# THE COFFEE MACHINE CODE 
#-----

def coffee_machine():
    coin = 0
    cup_sell = 0

    print("☕ Welcome to the Coffee Shop!")
    Coffee = [ 
        { 
            "Code": "A",
            "Name": "Cappuccino",
            "Half": 5,
            "Full": 10
        },
        { 
            "Code": "B",
            "Name": "Latte",
            "Half": 4,
            "Full": 8
        },
        { 
            "Code": "C",
            "Name": "Espresso",
            "Half": 3,
            "Full": 6
        },
        { 
            "Code": "D",
            "Name": "Mocha",
            "Half": 2,
            "Full": 4
        }
    ]

    while True:
        print("\nAvailable Coffee Options:")
        for coffee in Coffee:
            print(f"{coffee['Code']}: {coffee['Name']} - Half: ${coffee['Half']}, Full: ${coffee['Full']}")

        choice = input("Enter your coffee choice (A/B/C/D): ").strip().upper()

        # Find the coffee with matching code
        selected_coffee = None
        for coffee in Coffee:
            if coffee["Code"] == choice:
                selected_coffee = coffee
                break


        if selected_coffee is None:
            print("❌ Invalid choice. Please select from A, B, C, or D.")
            continue

        size = input("Enter your Cup Size (Half/Full): ").strip().capitalize()
        if size not in ["Half", "Full"]:
            print("❌ Invalid size. Please choose Half or Full.")
            continue

        price = selected_coffee[size]
        coin += price
        cup_sell += 1

        print(f"✅ You ordered a {size} cup of {selected_coffee['Name']}.")
        print(f"💵 Please pay ${price}.")
        print(f"📊 Total earnings: ${coin}, Cups sold: {cup_sell}")

        another = input("\nDo you want to order another coffee? (yes/no): ").strip().lower()
        if another != "yes":
            print("\n👋 Thank you for visiting the Coffee Shop!")
            break

# Run the coffee machine
coffee_machine()
