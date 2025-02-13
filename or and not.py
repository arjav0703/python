print("Heloo, welcome to networkchuck coffee!!!!!!!!!!!!!!")


name = input("What is your name? \n") 
if name == "Ben" or name == "Bob" or name == "Loki": #use or to add another condition
  #u can use not to negate the condition or use != to check if the condition is not true
  evil_status = input("Are you evil?\n")
  if evil_status != "No":
    good_deeds = int(input("How many good deeds have you done today?\n"))
  #the int() will convert the input into an integer for further calculation
    if evil_status == "Yes" and good_deeds <= 4:
    
     print("You have not done more than 4 good deeds Evil " + name + "!! Get out!!")
    
     exit()
  else:
    print("Oh, you have done your good deeds " + name + ". Come on in!!")
 
else:
  print("Hey " + name + ", thank you for coming in today")



print("So " + name + ", What would you like to have today?")
#drinks = "Coffee\nTea\nLatte\nCappucino\n"

#order = input(drinks)
#print("Sounds good " + name + ", we will have a " + order + " ready for you in a minute")