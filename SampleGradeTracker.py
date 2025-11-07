# Displaying the title and instructions for the user
print("-------- Weighted Course Grade Calculator --------")
print("\nInstructions: Enter the number of weighted assignments, then input each grade (0-100) and its weight (0-100). The total weight must not exceed 100. Use this calculator to determine your overall course grade, assess the impact of assignments, and track your academic progress throughout the semester.")

# Initialize an empty list to store each assignment's grade and weight
assignments = []

# Ask the user how many assignments or sections they want to enter
num = int(input("\nHow many weighted assignments/sections do you have? "))

# Track the total weight entered by the user to ensure it doesn't exceed 100
total_weight = 0

# Loop through each assignment
for i in range(num):
    print("\nAssignment/Section", i + 1)

    # Get a valid grade from the user (between 0 and 100)
    while True:
        grade = float(input("  Enter the grade (0-100): "))
        if 0 <= grade <= 100:
            break
        else:
            print("  Please enter a grade between 0 and 100.")

    # Get a valid weight from the user and ensure total doesn't exceed 100
    while True:
        weight = float(input("  Enter the weight: "))
        if 0 <= weight <= 100 and total_weight + weight <= 100:
            total_weight += weight
            break
        else:
            print("  Weight must be between 0 and 100 and total weights cannot exceed 100.")

    # Store the grade and weight as a dictionary and add to the list
    assignment = {"grade": grade, "weight": weight}
    assignments.append(assignment)


# Function to calculate the weighted overall grade
def calculate_grade(assignments):
    total = 0
    for a in assignments:
        # Multiply each grade by its weight and add to the total
        total += a["grade"] * a["weight"]
    
    # Check to avoid division by zero
    if total_weight == 0:
        print("  Weight must be between 0 and 100 and total weights cannot exceed 100.")
    else:
        overall = total / total_weight
        return overall


# Function to return a motivational message based on the final grade
def grade_message(grade):
    if grade >= 90:
        return "Great job! You're doing excellent!"
    elif grade >= 80:
        return "Good work! Keep it up!"
    elif grade >= 70:
        return "You're getting there, keep pushing!"
    else:
        return "Don't give up! You can improve!"


# Call the calculation function and print the result and message
overall = calculate_grade(assignments)
print("\nYour current overall grade is:", overall, "%")
print(grade_message(overall))

# Closing message
print("\nThanks for using the calculator! Good luck!")