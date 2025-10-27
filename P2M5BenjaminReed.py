# [] create Element_Quiz

##Download the data file for elements1_20.txt
import os

os.system ("curl -s -O https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt")

def get_names(): ## creates a function that gets the person's name, and gets input for the name of the element.
                 ## If the input is empty, it says space not allowed.
                 ## if it is a duplicate, it says no duplicates.
                 ## If it is a new input, it appemd it to the input_names list.

    input_names = []

    while len(input_names) < 5:
        name = input("Enter the name of an element: ").lower().strip()

        if name == "":
            print("Empty Space Not Allowed")

        elif name in input_names:

            print(f"{name} was already entered <--- no duplicates allowed")

        else:
            input_names.append(name)

    return input_names

## The program welcomes the user and asks for 5 elements.
your_name = input("Please enter your full name: ")
print(f"Welcome {your_name}, list any 5 of the first 20 elements in the Periodic Table: ")

first_20_elements = []

try: ## The program opens elements1_20.txt and reads one line at a time.
     ## The program also removes any whitespace, makes it lowercase, and appends to the first_20_elements list.

    elements_file = open('elements1_20.txt', 'r')

    for line in elements_file:

        first_20_elements.append(line.strip().lower())

    elements_file.close()

except FileNotFoundError: ## The code will exit the program and notify of the elements1_20.txt file was not found.
    print("Error: The file 'elements1_20.txt' was not found.")
    exit()

quiz_reponses = get_names() ## Call the get_names function.
correct_responses = [] ## Makes a list of correct responses.
incorrect_responses = [] ## Makes a list of incorrect repsonses.

for response in quiz_reponses: ## Now we iterate through the 5 reponses from the user input.
                               ## It comparess each response to the list of 20 elements.
    if response in first_20_elements:
                               ## If correct, the input is appended to the correct_response list.
        correct_responses.append(response)

    else:                      ## if the input is incorrect, it appends it to the incorrect_response list.
        incorrect_responses.append(response)

percent_correct = len(correct_responses) * 20 ## the list of correct_reponse times 20 gives the percent correct.
percent_correct = int(percent_correct) ##turns percent correct into an int.

BOLD = '\033[1m' ## makes text bold
RED = '\033[91m' ## Specifies the color red.
ENDC = '\033[0m'  ## Specifies the normal color.
B_GREEN = '\033[42m'

if percent_correct < 70: ##If the user scores less than 70%, the putput is red.
    COLOR = RED

else:
    COLOR = ENDC

print("\n" + "<>"*30)
print()
print(f"{COLOR}{BOLD}{percent_correct} % correct{ENDC}")

found_list = [f"{B_GREEN}{BOLD}{name.title()}{ENDC}" for name in correct_responses] ## turns correct responses into Title form for printing.

print("Found: ", end="")
print(', '.join(found_list)) ## Joins the found_list into a single string with spaces betweem.

not_found_list = [name.title() for name in incorrect_responses]## turns incorrect responses into Title form for printing.
print("Not Found: ", end="")
print(", ".join(not_found_list)) ## Joins the found_list into a single string with spaces betweem.

print()
print("<>"*30)