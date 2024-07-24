### using def to define a function

def My_List():
    my_lists = []
    while True:
        print("Welcome to List Manager. ")
        a = int(input('''
        What would ypu like to do:
        1. Adding an item in the list.
        2. Removing an item from the list.
        3. Viewing the items in the list.
        4. Exit
        Enter your choice:  '''))
        
        ### if,elif and else statement are used

        if a == 1:

            ### pop is used to remove items from the array
            item = input("Enter the item to add: ")
            items = item.split(", ")
            print(items)
            # my_list.append(items)
            my_lists.extend(items)
            print(f"'{item}' has been added to the list.")

            ### pop is used to remove items from the array
        elif a == 2:
            print(my_lists)
            a = my_lists.pop(int(input("What would you like to remove. ")))
            print(f"{a} has been removed. ")

        elif a == 3:
            print(my_lists)
        
        elif a == 4:
            print("Exiting...")
            break

        else:
            print("Invalid input. Try Again!")


if __name__ == "__main__":
    My_List()