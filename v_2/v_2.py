#imports
from colorama import Fore



################################# D       E       V #################################
################################# N   O   T   E   S #################################

#yo, can you build the complete function? ~ nvm done it myself.. like whole thing

#end

#global
todo_list = [] #leave empty

#placeholder funcs
## using pass you can just copy and paste the code later on above in functions and work from there. REMEMBER TO USE PASS
def example_function():
    pass


#functions
def add_to_do():
    todo = input("Adding {Fore.YELLOW}To-Do{Fore.RESET}: ")
    todo_list.append(todo)

def view_to_do():
    print(f"{Fore.YELLOW}To-Do's{Fore.RESET}: ")
    if len(todo_list) == 0: #check if there is something in list bro...
        print(f'Nothing to do bro, lazy fuccc')
    else:
        for item in todo_list:
            print("- "+item)

def complete_to_do():
     todo_c = input(f"Mark {Fore.YELLOW}To-Do{Fore.RESET} as complete: ")
     todo_list.remove(todo_c)
#loop to keep menu open

while True:
        view_to_do()
        #this is just to separate from menu
        print("+++++++++++++++++++++++++++++++++")
        #run menu so in loop:
        print(f"---------------------------------")
        print(f"{Fore.YELLOW}To-Do's{Fore.RESET} management system")
        print(f"[{Fore.BLUE}a{Fore.RESET}] Add {Fore.YELLOW}To-Do{Fore.RESET}")
        print(f"[{Fore.YELLOW}c{Fore.RESET}] [BUILDING...]Complete To-Do")
        print(f"[{Fore.RED}v{Fore.RESET}] View list of {Fore.YELLOW}To-Do's{Fore.RESET}")
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