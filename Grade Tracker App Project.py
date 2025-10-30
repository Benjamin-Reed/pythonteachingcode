# ----------------------------------------------------------------------
# 🐍 Pure Python Grade Tracker App with Category Weighting and Deletion
# ----------------------------------------------------------------------

# GLOBAL DATA STRUCTURES
grades = {}             # Structure: { 'Course Name': [ (score, category_name), ... ], ... }
category_weights = {}   # Structure: { 'Category Name': weight_percentage, ... }
FILE_NAME = 'grades_data.txt'
WEIGHTS_FILE_NAME = 'category_weights.txt' 

# ----------------------------------------------------------------------
## 1. Helper Functions (File I/O)

def load_grades():
    """Loads grades and category weights data from plain text files."""
    global grades, category_weights
    
    # --- Load Grades ---
    try:
        with open(FILE_NAME, 'r') as file:
            grades = {} 
            for line in file:
                # Format: CourseName,Score,CategoryName
                parts = line.strip().split(',')
                if len(parts) == 3:
                    course, score_str, category = parts
                    score = float(score_str)
                    course = course.title()
                    category = category.title()

                    if course not in grades:
                        grades[course] = []
                    grades[course].append((score, category))
            print(f"Loaded {len(grades)} courses from {FILE_NAME}.")
            
    except FileNotFoundError:
        print("No existing grades file found. Starting fresh.")
    except Exception:
        print("Error reading grades file. Starting fresh.")
    
    # --- Load Category Weights ---
    try:
        with open(WEIGHTS_FILE_NAME, 'r') as file:
            category_weights = {} 
            for line in file:
                # Format: CategoryName,Weight
                parts = line.strip().split(',')
                if len(parts) == 2:
                    category, weight_str = parts
                    weight = float(weight_str)
                    category_weights[category.title()] = weight
            print(f"Loaded {len(category_weights)} assignment categories from {WEIGHTS_FILE_NAME}.")
            
    except FileNotFoundError:
        print("No existing weights file found. Starting fresh.")
    except Exception:
        print("Error reading weights file. Starting fresh.")
    
    return grades, category_weights

def save_grades():
    """Saves the current grades and category weights data to plain text files."""
    global grades, category_weights
    
    # --- Save Grades ---
    try:
        with open(FILE_NAME, 'w') as file:
            for course, items in grades.items():
                for score, category in items:
                    # Write in the format: CourseName,Score,CategoryName
                    file.write(f"{course},{score},{category}\n")
        print(f"Grades saved to {FILE_NAME}.")
    except Exception as e:
        print(f"Error saving grades: {e}")

    # --- Save Category Weights ---
    try:
        with open(WEIGHTS_FILE_NAME, 'w') as file:
            for category, weight in category_weights.items():
                # Write in the format: CategoryName,Weight
                file.write(f"{category},{weight}\n")
        print(f"Category weights saved to {WEIGHTS_FILE_NAME}.")
    except Exception as e:
        print(f"Error saving weights: {e}")

# ----------------------------------------------------------------------
## 2. Core Logic Functions

def add_course(course_name):
    """Adds a new course to the grades dictionary."""
    course_name = course_name.title()
    if course_name not in grades:
        grades[course_name] = [] 
        print(f"Course '{course_name}' added.")
    else:
        print(f"Course '{course_name}' already exists.")

def delete_course(course_name):
    """Deletes a specified course from the grades dictionary."""
    global grades
    course_name = course_name.title()
    
    if course_name in grades:
        del grades[course_name] 
        print(f"Course '{course_name}' has been deleted. (Remember to save before exiting!)")
    else:
        print(f"Error: Course '{course_name}' not found.")

def add_grade(course_name, score, category_name):
    """Adds a specific grade item (score and category) to a course."""
    course_name = course_name.title()
    category_name = category_name.title()
    
    if course_name not in grades:
        print(f"Error: Course '{course_name}' not found. Please add the course first (Menu 1).")
        return

    # Handle new category type and its weight
    if category_name not in category_weights:
        print(f"'{category_name}' is a new assignment type.")
        while True:
            try:
                weight = float(input(f"Enter the percentage weight for ALL '{category_name}' assignments (e.g., 20): "))
                if 0 <= weight <= 100:
                    category_weights[category_name] = weight
                    print(f"Category '{category_name}' weight set to {weight}%.")
                    break
                else:
                    print("Weight must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number for the weight.")
                
    # Add the grade
    grades[course_name].append((score, category_name))
    print(f"Grade {score}% added to {course_name} under category '{category_name}'.")

def calculate_gpa(course_name):
    """Calculates the weighted average grade for a single course based on category weights."""
    course_name = course_name.title()
    if course_name not in grades or not grades[course_name]:
        return "N/A"

    category_scores = {} 
    
    # Organize scores by category
    for score, category in grades[course_name]:
        # Explicitly convert to string to avoid 'AttributeError: 'float' object has no attribute 'title''
        category = str(category).title() 
        if category not in category_scores:
            category_scores[category] = []
        category_scores[category].append(score)

    total_weighted_sum = 0
    total_category_weight = 0

    # Calculate average for each category and apply the category's weight
    for category, scores in category_scores.items():
        if category in category_weights:
            category_weight = category_weights[category]
            category_average = sum(scores) / len(scores)
            
            total_weighted_sum += (category_average * category_weight)
            total_category_weight += category_weight
            
            # Print detailed breakdown
            print(f"  > {category} Avg: {category_average:.2f}% (Weight: {category_weight}%)")

    # Final GPA calculation
    if total_category_weight > 0:
        final_gpa = total_weighted_sum / total_category_weight
        return f"{final_gpa:.2f}%"
    else:
        return "No grades in weighted categories."

# ----------------------------------------------------------------------
## 3. Main Application Loop

def grade_tracker_app():
    """The main user interface for the application."""
    load_grades() 

    while True:
        print("\n--- Grade Tracker Menu ---")
        print("1. Add a New Course")
        print("2. Add a Grade (Score and Category)")
        print("3. View Course GPA")
        print("4. View All Category Weights")
        print("5. Delete a Course 🗑️")
        print("6. Save and Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the course name: ")
            add_course(name)

        elif choice == '2':
            # Check if there are courses to add grades to
            if grades:
                print("\nAvailable Courses:", ", ".join(grades.keys()))
                course = input("Enter course name to add grade: ")
                category = input("Enter assignment type (e.g., Quiz, Test, Homework): ")
                try:
                    score = float(input(f"Enter score for {category} (e.g., 92.5): "))
                    add_grade(course, score, category)
                except ValueError:
                    print("Invalid input for score. Please use a number.")
            else:
                print("Please add a course first (Menu 1).")

        elif choice == '3':
            if grades:
                print("\nAvailable Courses:", ", ".join(grades.keys()))
                course = input("Enter course name to view GPA: ")
                print(f"\n--- GPA Calculation for {course.title()} ---")
                gpa = calculate_gpa(course)
                print(f"\nFINAL GPA for {course.title()}: **{gpa}**")
            else:
                print("No courses available to calculate GPA.")

        elif choice == '4':
            print("\n--- Current Assignment Category Weights ---")
            if category_weights:
                for cat, weight in category_weights.items():
                    print(f"  > {cat}: {weight}%")
            else:
                print("No categories defined yet.")

        elif choice == '5':
            if grades:
                print("\nAvailable Courses:", ", ".join(grades.keys()))
                course_to_delete = input("Enter the course name to DELETE: ")
                delete_course(course_to_delete)
            else:
                print("No courses available to delete.")

        elif choice == '6':
            save_grades() 
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# ----------------------------------------------------------------------

# Run the application
if __name__ == "__main__":
    grade_tracker_app()