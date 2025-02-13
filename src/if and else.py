print("Heloo, welcome to networkchuck coffee!!!!!!!!!!!!!!")

#if ben comes, then he will get a kick
name = input("What is your name? \n") 
if name == "Ben":
  evil_status = input("Are you evil?\n")
  if evil_status == "Yes":
     print("You are not welcome here EvilBen!! Get out!!")
    
     exit()
  else:
    print("Oh, so you are one of those good Bens. Come on in!!")
  #the exit() will stop the execution of upcoming code
else:
  print("Hey " + name + ", thank you for coming in today")



print("So " + name + ", What would you like to have today?")
drinks = "Coffee\nTea\nLatte\nCappucino\n"

order = input(drinks)
print("Sounds good " + name + ", we will have a " + order + " ready for you in a minute")