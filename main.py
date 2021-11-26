import tkinter # to create the gui 
import random #to shuffle the list, and pick a random task


# dictionary for having a record of all users task 
choice_dict = {} 
usr_choice = "" # will contain what the user type 

print("Type the task that you want to work on, and then it's priority\nPress 'q' when you're done !")
# while loop to get the user's differents tasks and its respective priority
while usr_choice.lower() != "q":
    usr_choice = input("Please enter the task name ")
    if usr_choice !='q':
        priority = int(input("Please enter the task priority (only integers) "))
        choice_dict[usr_choice] = priority # add the task to the dictionary
    else :
        break

choice_list = [] # list that will be used to randomly choose tasks
for key in choice_dict : 
    for k in range(choice_dict[key]): 
        choice_list.append(key)
    print(f"The task {key} will be added to the list {choice_dict[key]} times ")

# put the tasks at random positions in the list
random.shuffle(choice_list)
print(f"You will have to do the tasks {choice_list[random.randint(len(choice_list))]}")