



def list_o_matic(item_list, item_string):

    if item_string == "":

        if item_list:
            popped_item = item_list.pop()
            return f"{popped_item} popped from list"
        else:
            return "List is already empty."
        
    elif item_string in item_list:

        item_list.remove(item_string)
        return f"1 instance of {item_string} removed from list."
    
    else:

        item_list.append(item_string)
        return f"1 instance of {item_string} appended to list."

colors_list = ['red','orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'magenta']
program_name = "colors"
my_name = "Benjamin Reed"

while True:

    if not colors_list:
        print("Goodbye")
        break

    print(f"\nWelcome, {my_name}. Look at all the {program_name} {colors_list}")

    color_input = input(f"Enter a color: ")

    if color_input == "quit":
        print("Goodbye!")
        break

    message = list_o_matic(colors_list, color_input)

    print(message)