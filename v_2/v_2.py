#imports
from colorama import Fore



################################# D       E       V #################################
################################# N   O   T   E   S #################################

#yo, can you build the complete function?

#end

#global
todo_list = [] #leave empty

#placeholder funcs
## using pass you can just copy and paste the code later on above in functions and work from there. REMEMBER TO USE PASS
def complete_to_do():
    pass


#functions
def add_to_do():
    todo = input("Adding To-Do: ")
    todo_list.append(todo)

def view_to_do():
    print(f"To-Do's: ")
    if len(todo_list) == 0: #check if there is something in list bro...
        print(f'Nothing to do bro, lazy fuccc')
    else:
        for item in todo_list:
            print("- "+item)

#loop to keep menu open

while True:
        view_to_do()
        #this is just to separate from menu
        print("+++++++++++++++++++++++++++++++++")
        #run menu so in loop:
        print(f"---------------------------------")
        print(f"{Fore.YELLOW}TO-DOs{Fore.RESET} management system")
        print(f"[{Fore.BLUE}a{Fore.RESET}] Add To-Do")
        print(f"[{Fore.YELLOW}c{Fore.RESET}] [BUILDING...]Complete To-Do")
        print(f"[{Fore.RED}v{Fore.RESET}] View list of To-Do's")
        print(f"---------------------------------")
        choice = input("Please select an option!('q' to quit): ")#detects input from user
        if choice == "1":
            view_to_do()
        elif choice == "c".lower():
            complete_to_do()
        elif choice == "a".lower(): # i will use .lower so if user input is capital or not will work anyway
                add_to_do()
        elif choice == "q".lower():
            break #i assume you know what this does..