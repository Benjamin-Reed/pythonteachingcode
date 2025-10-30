# ----------------------------------------------------------------------
# 🐍 COMPLETE COURSE-SPECIFIC WEIGHTED GRADE TRACKER APP
#    Features: Course-specific category weights, Add/Delete Course, 
#              Single GPA breakdown, All GPA summary.
# ----------------------------------------------------------------------

# GLOBAL DATA STRUCTURES
# Structure:
# grades = { 
#    'Course Name': {
#        'grades': [ (score, category_name), ... ],
#        'weights': { 'Category Name': weight_percentage, ... }
#    },
# }
grades = {}             
FILE_NAME = 'grades_data.txt'

# ----------------------------------------------------------------------
## 1. Helper Functions (Pure Python File I/O)

def load_grades():
    """Loads grades data from a plain text file, rebuilding the nested structure."""
    global grades
    
    try:
        with open(FILE_NAME, 'r') as file:
            grades = {} 
            for line in file:
                # Format: CourseName,Score,CategoryName,CategoryWeight
                parts = line.strip().split(',')
                if len(parts) == 4: 
                    course, score_str, category, weight_str = parts
                    score = float(score_str)
                    weight = float(weight_str)
                    course = course.title()
                    category = category.title()

                    # Rebuild the nested dictionary structure
                    if course not in grades:
                        grades[course] = {'grades': [], 'weights': {}} 
                    
                    grades[course]['grades'].append((score, category))
                    grades[course]['weights'][category] = weight 
                    
            print(f"Loaded {len(grades)} courses from {FILE_NAME}.")
            
    except FileNotFoundError:
        print("No existing grades file found. Starting fresh.")
    except Exception:
        print("Error reading grades file. Data might be corrupt. Starting fresh.")

def save_grades():
    """Saves all courses, grades, and their course-specific weights to one text file."""
    global grades
    
    try:
        with open(FILE_NAME, 'w') as file:
            for course, data in grades.items():
                course_weights = data['weights']
                
                # Check if course has any grades before saving
                if data['grades']:
                    for score, category in data['grades']:
                        # The weight must exist since it was required during add_grade
                        weight = course_weights[category]
                        
                        # Write in the format: CourseName,Score,CategoryName,CategoryWeight
                        file.write(f"{course},{score},{category},{weight}\n")
        print(f"Grades and course-specific weights saved to {FILE_NAME}.")
    except Exception as e:
        print(f"Error saving grades: {e}")

# ----------------------------------------------------------------------
## 2. Core Logic Functions

def add_course(course_name):
    """Adds a new course, initializing its nested data structure."""
    course_name = course_name.title()
    if course_name not in grades:
        grades[course_name] = {'grades': [], 'weights': {}} 
        print(f"Course '{course_name}' added.")
    else:
        print(f"Course '{course_name}' already exists.")

def delete_course(course_name):
    """Deletes a specified course and all its grades/weights."""
    global grades
    course_name = course_name.title()
    
    if course_name in grades:
        del grades[course_name] 
        print(f"Course '{course_name}' has been deleted. (Remember to save before exiting!)")
    else:
        print(f"Error: Course '{course_name}' not found.")

def add_grade(course_name, score, category_name):
    """Adds a grade, checks for course-specific category weight, and prompts if needed."""
    course_name = course_name.title()
    category_name = category_name.title()
    
    if course_name not in grades:
        print(f"Error: Course '{course_name}' not found. Please add the course first (Menu 1).")
        return

    course_weights = grades[course_name]['weights']
    
    # Handle new category type and its course-specific weight
    if category_name not in course_weights:
        print(f"'{category_name}' is a NEW assignment type for {course_name}.")
        while True:
            try:
                weight = float(input(f"Enter the percentage weight for ALL '{category_name}' assignments in {course_name} (e.g., 20): "))
                if 0 <= weight <= 100:
                    course_weights[category_name] = weight
                    print(f"Category '{category_name}' weight set to {weight}% for {course_name}.")
                    break
                else:
                    print("Weight must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number for the weight.")
                
    # Add the grade to the course's grades list
    grades[course_name]['grades'].append((score, category_name))
    print(f"Grade {score}% added to {course_name} under category '{category_name}'.")

def calculate_gpa(course_name, show_breakdown=True):
    """Calculates the weighted average grade for a single course. 
       If show_breakdown is True, prints the category details."""
    course_name = course_name.title()
    if course_name not in grades or not grades[course_name]['grades']:
        return "N/A"

    course_data = grades[course_name]
    course_weights = course_data['weights']
    
    category_scores = {} 
    
    # 1. Organize scores by category
    for score, category in course_data['grades']:
        category = str(category).title() 
        if category not in category_scores:
            category_scores[category] = []
        category_scores[category].append(score)

    total_weighted_sum = 0
    total_category_weight = 0

    # 2. Calculate average for each category and apply the course's specific weight
    for category, scores in category_scores.items():
        if category in course_weights:
            category_weight = course_weights[category]
            category_average = sum(scores) / len(scores)
            
            total_weighted_sum += (category_average * category_weight)
            total_category_weight += category_weight
            
            if show_breakdown:
                print(f"  > {category} Avg: {category_average:.2f}% (Weight: {category_weight}%)")

    # 3. Final GPA calculation
    if total_category_weight > 0:
        final_gpa = total_weighted_sum / total_category_weight
        return f"{final_gpa:.2f}%"
    else:
        return "No grades in weighted categories."

def calculate_all_gpas():
    """Calculates and prints the weighted average GPA for all stored courses."""
    global grades
    
    if not grades:
        print("No courses added yet.")
        return

    print("\n--- Summary of All Course GPAs 📈 ---")
    print("-----------------------------------")
    
    for course_name in grades.keys():
        # Call calculate_gpa with show_breakdown=False to avoid clutter
        gpa_result = calculate_gpa(course_name, show_breakdown=False) 
        print(f"  > {course_name}: {gpa_result}")
        
    print("-----------------------------------")

# ----------------------------------------------------------------------
## 3. Main Application Loop

def grade_tracker_app():
    """The main user interface for the application."""
    load_grades() 

    while True:
        print("\n--- Grade Tracker Menu ---")
        print("1. Add a New Course")
        print("2. Add a Grade (Score and Category)")
        print("3. View GPA for ALL Courses 📈")
        print("4. View GPA for a Single Course (with Breakdown)")
        print("5. View Course Category Weights")
        print("6. Delete a Course 🗑️")
        print("7. Save and Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter the course name: ")
            add_course(name)

        elif choice == '2':
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
            calculate_all_gpas()

        elif choice == '4':
            if grades:
                print("\nAvailable Courses:", ", ".join(grades.keys()))
                course = input("Enter course name to view GPA: ")
                print(f"\n--- GPA Calculation for {course.title()} ---")
                # Call calculate_gpa with default show_breakdown=True
                gpa = calculate_gpa(course) 
                print(f"\nFINAL GPA for {course.title()}: **{gpa}**")
            else:
                print("No courses available to calculate GPA.")

        elif choice == '5':
            if grades:
                print("\nAvailable Courses:", ", ".join(grades.keys()))
                course_to_view = input("Enter course name to view weights: ").title()
                
                if course_to_view in grades:
                    weights = grades[course_to_view]['weights']
                    print(f"\n--- {course_to_view} Category Weights ---")
                    if weights:
                        for cat, weight in weights.items():
                            print(f"  > {cat}: {weight}%")
                    else:
                        print(f"No categories defined for {course_to_view} yet.")
                else:
                    print(f"Error: Course '{course_to_view}' not found.")
            else:
                print("No courses available to view weights.")

        elif choice == '6':
            if grades:
                print("\nAvailable Courses:", ", ".join(grades.keys()))
                course_to_delete = input("Enter the course name to DELETE: ")
                delete_course(course_to_delete)
            else:
                print("No courses available to delete.")

        elif choice == '7':
            save_grades() 
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

# ----------------------------------------------------------------------

# Run the application
if __name__ == "__main__":
    grade_tracker_app()