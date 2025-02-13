print("Heloo, welcome to networkchuck coffee!!!!!!!!!!!!!!")

# This will ask the user to enter an input
#input("what is your name?") 


#combine the print and input functions and it will ask the user to input and will print the input
#print(input("what is your name?"))


#Variable
#name = "coffeelover"
#print(name)

#this will ask the user to input and will print the input aloong with the string that is greeting
name = input("What is your name? \n") 
print("Hey " + name + ", thank you for coming in today")

print("So " + name + ", What would you like to have today?")
drinks = "Coffee\nTea\nLatte\nCappucino\n"
input(drinks)

order = input(drinks)
print("Sounds good " + name + ", we will have a " + order + " ready for you in a minute")