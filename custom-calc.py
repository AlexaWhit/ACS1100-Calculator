# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

print("Welcome to the Discount Calculator!")
price_str = input("What is the price of the item? ")
percentage_str = input("Please enter the discount percentage (ex. 20 discount = 20) : ")
quantity_str = input("Please enter how many items of the items you would like to buy (ex. if you would like to purchase 4, then enter 4) : ")

original_price = float(price_str) 
percentage = float(percentage_str) 
quantity = int(quantity_str)

discount = float(percentage / 100)
discount_dollars = float(original_price * discount)

sales_price = float(original_price - discount_dollars)

print(f"The final price of the item(s) is: ${sales_price * quantity}")

#I had a hard time utilizing three inputs, and I may have made this too difficult for myself, but it works!




