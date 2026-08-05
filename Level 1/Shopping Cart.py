print("========================================")
print("         Pixel Gear Gaming Store        ")
print("========================================")


peripherals = ["Gaming Mouse", "Mechanical Keyboard", "Headset", "Mousepad"]
p_prices = [1499.99, 3299.99, 2199.99, 499.99]

components = ["16GB RAM", "1TB NVMe SSD", "750W Power Supply"]
c_prices = [3499.99, 5999.99, 4499.99]
accessories = ["Webcam", "Stream Deck", "RGB Light Strip"]
a_prices = [1899.99, 8999.99, 799.99]

discount_codes = ["GAMER10", "WELCOME15", "PRO20", "SUPER50"]
discount_rates = [0.10, 0.15, 0.30, 0.50]

cart_names = []
cart_counts = []
cart_prices = []

running = True


while running == True:
    print("\n--- PRODUCT CATEGORIES ---")
    print("1. Peripherals")
    print("2. PC Parts")
    print("3. Streaming")
    print("4. View Cart")
    print("5. Checkout")
    
    cat_choice = input("Select an option (1-5): ")

    if cat_choice == "1":
        print("\n--- PERIPHERALS ---")
        for i in range(len(peripherals)):
            print(i + 1, "-", peripherals[i], ": Rs.", p_prices[i])
        
        item_num = int(input("Enter item number: "))

        if item_num >= 1 and item_num <= len(peripherals):
            selected_item = peripherals[item_num - 1]
            selected_price = p_prices[item_num - 1]
            
            already_in_cart = 0
            for x in range(len(cart_names)):
                if cart_names[x] == selected_item:
                    already_in_cart = cart_counts[x]


            valid_qty = False
            while valid_qty == False:
                qty = int(input("Enter quantity (Max 10): "))
                if qty <= 0:
                    print("Error: Quantity must be at least 1! Please re-enter.")
                elif already_in_cart + qty > 10:
                    print("Error: Total quantity cannot exceed 10! You already have", already_in_cart, "in cart. Please re-enter.")
                else:
                    valid_qty = True
            
            found = False
            for x in range(len(cart_names)):
                if cart_names[x] == selected_item:
                    cart_counts[x] = cart_counts[x] + qty
                    found = True
            
            if found == False:
                cart_names.append(selected_item)
                cart_counts.append(qty)
                cart_prices.append(selected_price)
                
            print(qty, "x", selected_item, "added!")
        else:
            print("Invalid item number!")

    elif cat_choice == "2":
        print("\n--- PC COMPONENTS ---")

        for i in range(len(components)):
            print(i + 1, "-", components[i], ": Rs.", c_prices[i])
        
        item_num = int(input("Enter item number: "))
        if item_num >= 1 and item_num <= len(components):
            selected_item = components[item_num - 1]
            selected_price = c_prices[item_num - 1]
            
            already_in_cart = 0
            for x in range(len(cart_names)):
                if cart_names[x] == selected_item:
                    already_in_cart = cart_counts[x]

            valid_qty = False
            while valid_qty == False:
                qty = int(input("Enter quantity (Max 10): "))
                if qty <= 0:
                    print("Error: Quantity must be at least 1! Please re-enter.")
                elif already_in_cart + qty > 10:
                    print("Error: Total quantity cannot exceed 10! You already have", already_in_cart, "in cart. Please re-enter.")
                else:
                    valid_qty = True


            found = False
            for x in range(len(cart_names)):
                if cart_names[x] == selected_item:
                    cart_counts[x] = cart_counts[x] + qty
                    found = True

            if found == False:
                cart_names.append(selected_item)
                cart_counts.append(qty)
                cart_prices.append(selected_price)
                
            print(qty, "x", selected_item, "added!")
        else:
            print("Invalid item number!")

    elif cat_choice == "3":
        print("\n--- STREAMING ACCESSORIES ---")
        for i in range(len(accessories)):
            print(i + 1, "-", accessories[i], ": Rs.", a_prices[i])

        item_num = int(input("Enter item number: "))
        if item_num >= 1 and item_num <= len(accessories):
            selected_item = accessories[item_num - 1]
            selected_price = a_prices[item_num - 1]
            
            already_in_cart = 0
            for x in range(len(cart_names)):
                if cart_names[x] == selected_item:
                    already_in_cart = cart_counts[x]

            valid_qty = False
            while valid_qty == False:
                qty = int(input("Enter quantity (Max 10): "))
                if qty <= 0:
                    print("Error: Quantity must be at least 1! Please re-enter.")
                elif already_in_cart + qty > 10:
                    print("Error: Total quantity cannot exceed 10! You already have", already_in_cart, "in cart. Please re-enter.")
                else:
                    valid_qty = True

            found = False
            for x in range(len(cart_names)):
                if cart_names[x] == selected_item:
                    cart_counts[x] = cart_counts[x] + qty
                    found = True
            
            if found == False:
                cart_names.append(selected_item)
                cart_counts.append(qty)
                cart_prices.append(selected_price)
                
            print(qty, "x", selected_item, "added!")
        else:
            print("Invalid item number!")


    elif cat_choice == "4":
        print("\n--- YOUR CART ---")
        if len(cart_names) == 0:
            print("Your cart is empty.")
        else:
            for c in range(len(cart_names)):
                print(cart_names[c], "x", cart_counts[c])

    elif cat_choice == "5":
        running = False

    else:
        print("Invaled choice, try again.")


print("\n========================================")
print("            PRELIMNARY RECEIPT         ")
print("========================================")

subtotal = 0.0
for k in range(len(cart_names)):
    name = cart_names[k]
    u_price = cart_prices[k]
    total_p = u_price * cart_counts[k]
    subtotal = subtotal + total_p
    print(name)
    print("  Qty:", cart_counts[k], " Price:", u_price, " Sub:", round(total_p, 2))

print("Subtotal: Rs.", round(subtotal, 2))


if subtotal > 0:
    next_5000 = 5000 * (subtotal // 5000 + 1)
    gap_5000 = next_5000 - subtotal

    print("\nIf you purchas for Rs.", round(next_5000, 2), "you will get an extra 10% upsell discount!")
    discount_wanted = input("Would you like to take this offer? (Y/N): ")

    if discount_wanted == "Y" or discount_wanted == "y":
        all_items = peripherals + components + accessories
        all_prices = p_prices + c_prices + a_prices

        print("\nYou have the following options to reach the limit:")
        add_quant = []
        for kk in range(len(all_items)):
            needed = int(gap_5000 // all_prices[kk] + 1)
            add_quant.append(needed)
            print(kk + 1, ". Add", all_items[kk], "-", needed, "units")
        
        add_on = int(input("Please indicate your preferance (1-" + str(len(all_items)) + "): ")) 
        if add_on >= 1 and add_on <= len(all_items):
            chosen_item = all_items[add_on - 1]
            chosen_price = all_prices[add_on - 1]
            chosen_qty = add_quant[add_on - 1]

            already_in_cart = 0
            for x in range(len(cart_names)):
                if cart_names[x] == chosen_item:
                    already_in_cart = cart_counts[x]

            if already_in_cart + chosen_qty > 10:
                print("Sorry, adding", chosen_qty, "units would exceed the maximum limit of 10 for this item!")
                print("Upsell offer cancelled. Proceeding to final checkout.")
                upsell_applied = False
            else:
                found = False
                for x in range(len(cart_names)):
                    if cart_names[x] == chosen_item:
                        cart_counts[x] = cart_counts[x] + chosen_qty
                        found = True
                
                if found == False:
                    cart_names.append(chosen_item)
                    cart_counts.append(chosen_qty)
                    cart_prices.append(chosen_price)
                    
                print("Shopping cart updated successfully!")
                upsell_applied = True
        else:
            print("Invalid option! Proceeding to checkout without upsell.")
            upsell_applied = False
    else:
        upsell_applied = False
        print("Proceeding to checkout...")
else:
    upsell_applied = False


print("\n========================================")
print("            FINAL RECEIPT               ")
print("========================================")

subtotal = 0.0
for k in range(len(cart_names)):
    name = cart_names[k]
    u_price = cart_prices[k]
    total_p = u_price * cart_counts[k]
    subtotal = subtotal + total_p
    print(name)
    print("  Qty:", cart_counts[k], " Price:", u_price, " Sub:", round(total_p, 2))


promo_discount = 0.0
print()
promo = input("Do you have a discount code? (enter the code or press Enter to skip): ")

if promo != "":
    if promo in discount_codes:
        code_index = discount_codes.index(promo)
        rate = discount_rates[code_index]
        promo_discount = subtotal * rate
        print("Promo code applied! You got", str(int(rate * 100)) + "% off.")
    else:
        print("Invalid promo code. No discount has been applied.")

upsell_discount = 0.0
if upsell_applied == True:
    upsell_discount = subtotal * 0.10
    print("Special upsell offer applied! Extra 10% off.")


total_discount = promo_discount + upsell_discount
tax = (subtotal - total_discount) * 0.18
final_total = subtotal - total_discount + tax

print("\n----------------------------------------")
print("Subtotal:        Rs.", round(subtotal, 2))
print("Promo Discount: -Rs.", round(promo_discount, 2))
print("Upsell Discount:-Rs.", round(upsell_discount, 2))
print("Tax GST (18%):       Rs.", round(tax, 2))
print("TOTAL:           Rs.", round(final_total, 2))
print("----------------------------------------")

print("Thank you for shoping at Pixe;!")