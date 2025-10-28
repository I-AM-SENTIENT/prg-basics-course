price = float(input("Input the price: "))
discount = float(input("Input the discount in %: "))

discount_amount = price * (discount/100)
price_after_discount = price - discount_amount

discount_amount = round(discount_amount,2)
price_after_discount = round(price_after_discount,2)


print(f"Price with discount {price_after_discount}")
print(f"Reduction {discount_amount}")