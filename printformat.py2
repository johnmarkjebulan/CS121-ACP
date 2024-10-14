def discount_calculator():
    while True:
        try:
            total_amount = float(input("Enter the total purchase amount: "))
            if total_amount < 0:
                print("Please enter a positive amount.")
                continue
            
            discount_percentage = 10 if total_amount > 5000 else 5
            
            discount_amount = (discount_percentage / 100) * total_amount
            final_price = total_amount - discount_amount
            
            print(f"\nInitial Purchase Amount: {total_amount:.2f}")
            print(f"Discount: {discount_percentage}% {discount_amount:.2f}")
            print(f"Final Price: {final_price:.2f}\n")
        
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue
        
        try_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Maraming Salamat!")
            break
        
discount_calculator()
