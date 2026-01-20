original_price = float(input("ENTER ORIGINAL PRICE: "))

discount_percentage = float(input("ENTER DISCOUNT PERCENTAGE: "))

discount_price = original_price - (original_price * discount_percentage / 100)

print(f"THE FINAL PRICE OF THE ITEM AFTER A {discount_percentage}% IS: {discount_price}")