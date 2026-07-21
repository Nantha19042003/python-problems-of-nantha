Question:

An online food delivery company wants to calculate the customer's final bill. The customer enters the total food amount. If the order amount is ₹1000 or more, the customer gets a 20% discount. Otherwise, no discount is given. Write a Python program to calculate and display the discount and final payable amount.

Answer:

print("===== ONLINE FOOD DELIVERY BILL =====")

customer = input("Enter Customer Name: ")
amount = float(input("Enter Food Order Amount: "))

if amount >= 1000:
    discount = amount * 20 / 100
else:
    discount = 0

final_amount = amount - discount

print("\nCustomer Name :", customer)
print("Order Amount :", amount)
print("Discount :", discount)
print("Final Payable Amount :", final_amount)
