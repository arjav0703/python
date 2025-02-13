
#lists

#camping_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, flash drive"
#print(camping_stuff)

#PYTHON lists

camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive"]
# print(type(camping_list))
camp_site = ["Crystal Lake", 404, 89.3, True]
#Crystal Lake is a string, 404 is an integer, 89.3 is a float, and True is a boolean
#a list can contain different data types


me = camping_list[4] #start counting from 0

you = camping_list[-1] #using negative numbers starts counting from the end of the list
#print(camping_list[-5])
#print(me) 
#print(you)

################################/\  | \ | \ ###############
###############################/  \ |_/ |_/ ################
###################################APPEND##################
#list methods
camping_list.append("toilet paper")
camping_list.append("Soap") 
#only 1 item can be added at a time


##################################EXTEND####################################
camping_list.extend(["face wash", "sanitiizer"]) #add another list inside the list

#################################ADD####################################
camping_list = camping_list + ["laptop", "charger"] #+ camp_site 
#add lists using variable or typing that

#################################INSERT####################################
camping_list.insert(-1, "matchstick") 
#add stuff to a specific place in the list
#print(camping_list)


##########################################################################
##############################################################################
#################################CLEAR###########################################

#camping_list.clear() ######Takes out entire list
#print(camping_list)

##################################REMOVE#####################################

camping_list.remove("tent") #remove specific item

camping_list.remove(camping_list[5]) #5=ethernet cable #remove using index

#print(camping_list)

##################################POP#####################################

#camping_list.pop(0)
#YOU CAN ALSO USE POP TO REMOVE AND STORE THAT IN A VARIABLE
print("Python deleted " + camping_list.pop(0) + " using POP method")
print(camping_list)