def calculate_discount(price, discount_percent):
    
    if discount_percent<=20:
        final_price= price- (total_discount)
    else:
        final_price= price
    return final_price

price=int(input("Enter the original price\n"))
discount_percent= int(input("Enter the discount percentage\n"))
total_discount= price * (discount_percent/100)

print("The discount is ", total_discount)
print("The final price is:", calculate_discount(price,discount_percent))
