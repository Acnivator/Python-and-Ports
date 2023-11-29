while True:
    total = 0
    customer_name = input("Enter customer name: ")

    while True:
        quantity = int(input("Enter the quantity of item: "))
        item_price = float(input("Enter the price per item: "))

        item_total = quantity * item_price

        total += item_total

        repeat = input("Do you want to add more items? (Y/y/N/n): ")

        if repeat.lower() != 'y':
            break  

    print("\n===== Bill for", customer_name, "=====")
    print("Items\t\tQuantity\tPrice\t\tTotal")
    print(f"Item 1\t\t{quantity}\t\t{item_price}\t\t{item_total}")

    print("\nTotal Amount:", total)

    new_customer = input("Is there a new customer in the queue? (Y/y/N/n): ")

    if new_customer.lower() != 'y':
        break  
