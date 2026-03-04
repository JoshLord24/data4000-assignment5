# This is a Point of Sale system 

def main():

    # Get the student key and calculate the seed
    student_key = input("Enter your student key: ")

    seed = sum(ord(ch) for ch in student_key.strip()) 

    subtotal = 0.0
    total_units = 0

    # Loop to get item details from the user
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == "done":
            break
        if item_name == "":
            print("Item name cannot be empty. Please try again.")
            continue
        while True:
            try:
                unit_price = float(input("Enter unit price: "))
                if unit_price < 0:
                    print("Unit price cannot be negative. Please try again.")
                    continue
            except ValueError:
                print("Invalid input for unit price. Please enter a valid number.")
                continue
            break
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity < 1:
                    print("Quantity must be at least 1. Please try again.")
                    continue
            except ValueError:
                print("Invalid input for quantity. Please enter a valid integer.")
                continue
            break

    # Calculate the subtotal for the current item and update totals
        def calculate_subtotal(unit_price, quantity):
            return unit_price * quantity
        subtotal += calculate_subtotal(unit_price, quantity)
        total_units += quantity

    # Calculates the discount 
    def calculate_discount(total_units, subtotal):
        if total_units >= 10 or subtotal >= 100:
            discount = 0.1
        else:
            discount = 0.0
        discount_amount = subtotal * discount
        total = subtotal - discount_amount
        return discount_amount, total

    #Checks if the customer gets a perk based on seed
    def perk_check(seed, total):
        perk = "No"
        if seed % 2 == 0:
            total -= 3.00
            perk = "Yes"
        return perk, total

    #function to calculate the discount and check for perks
    discount_amount, total = calculate_discount(total_units, subtotal)
    perk, total = perk_check(seed, total)

    #prints outs results
    print(f"Seed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount_amount:.2f}")
    print(f"Perk applied: {perk}")
    print(f"Total: ${total:.2f}")


main()
