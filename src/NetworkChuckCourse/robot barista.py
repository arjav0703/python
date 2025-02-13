import time  # Importing the time module to allow the use of time.sleep(), which can pause the program for a spe

print("Heloo, welcome to techy coffee!!!!!!!!!!!!!!")  # Print a welcome message

## USE OF VERIABLES ##

# Asking the user for their first name and storing it in a variable 'name'
# used INPUT function
name = input('Can we get your first name please?\n')  ## \n is used to move to the next Line ##

## USAGE OF STRING CONCATENATION ##
print("So " + name + ", What would you like to have today?\n \nWE HAVE THE FOLLOWING ITEMS ON OUR MENU")

# Defining the menu options available for selection
drinks = "\n 1. Coffee $4/$2\n 2. Tea $3/$5\n 3. Latte $7\n 4. Cappucino $10\n\n"

# Storing response in the 'order' variable
order = input(drinks)

# Conditional statements to determine the price based on the user's selection
if order == "Coffee":  # If the user chooses Coffee
  coffee_whiped = input("\nDo you want whipped cream? (y/n)\n")  # Asking if they want whipped cream
  if coffee_whiped == "y":  # If the user wants whipped cream
    price = 4  # Set the price to $4 for Coffee with whipped cream
  else:  # If the user does not want whipped cream
    price = 2  # Set the price to $2 for Coffee without whipped cream

elif order == "Tea":  # If the user chooses Tea
  tea_type = input("Do you want black or green tea?\n")  # Asking the user for tea preference
  if tea_type == "Black":  # If the user chooses Black tea
    price = 3  # Set the price to $3 for Black tea
  else:  # If the user chooses any other option (assumed to be Green tea)
    price = 5  # Set the price to $5 for Green tea

elif order == "Latte":  # If the user chooses Latte
  price = 7  # Set the price to $7 for Latte

elif order == "Cappucino":  # If the user chooses Cappuccino
  price = 10  # Set the price to $10 for Cappuccino

else:  # If the user inputs something not on the menu
  print("Sorry, we don't have that here. Please select from the following")  
  exit()


quantity = input("How many " + order + " would you like?\n")  

print("Sounds good " + name + ", we will have " + quantity + " " +   order + " ready for you in a minute")

# Calculating the total bill by multiplying the price by the quantity ordered
bill = price * int(quantity)  # Convert the quantity input (string) to an integer and multiply by the price

time.sleep(2)  # Pause the program for 2 seconds to simulate processing time

print("Here is your " + order + " and your total is $" + str(bill))  # Convert the bill to a string for concatenation and display
