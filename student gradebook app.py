import csv
import os

# Configuration: Define the file name where records will be stored
FILE_NAME = "student_gradebook.csv"

def calculate_grade(marks):
    """Calculates and returns the letter grade based on numeric marks."""
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def add_student():
    """Asks for student details, calculates their grade, and saves to the CSV file."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.\n")
        return
        
    try:
        # Prompt for marks and convert to a floating-point number
        marks = float(input("Enter student marks (0-100): "))
        
        # Validate that marks fall within a realistic percentage range
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.\n")
            return
            
        grade = calculate_grade(marks)
        
        # Check if file exists AND has content to determine if we need headers
        # Fixed: Checking os.path.getsize ensures headers write if the file was created blank
        file_exists = os.path.isfile(FILE_NAME) and os.path.getsize(FILE_NAME) > 0
        
        # Open file in append mode ('a') so we don't overwrite existing records
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write column headers if this is a brand new or empty file
            if not file_exists:
                writer.writerow(["Name", "Marks", "Grade"])
                
            writer.writerow([name, marks, grade])
            
        print(f"Success: Record for '{name}' added successfully!\n")
        
    except ValueError:
        # Handles cases where the user inputs text instead of a number for marks
        print("Error: Invalid input. Marks must be a numeric value.\n")
    except PermissionError:
        # Handles cases where the CSV file is locked (e.g., open in Microsoft Excel)
        print(f"Error: Permission denied. Please close '{FILE_NAME}' if it is open in another program.\n")
    except Exception as e:
        # Catch-all block for any other unexpected operating system or file errors
        print(f"An unexpected error occurred: {e}\n")

def view_records():
    """Reads and cleanly displays all student records from the CSV file."""
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            
            # Try to skip the header row. If the file is completely empty, this raises StopIteration
            try:
                headers = next(reader)
            except StopIteration:
                print("\nThe gradebook file is empty.\n")
                return
                
            print(f"\n{'='*40}")
            print(f"{'Name':<20} {'Marks':<10} {'Grade':<10}")
            print(f"{'='*40}")
            
            has_records = False
            for row in reader:
                # Ensure the row has exactly 3 columns to avoid tracking broken or corrupted data rows
                if len(row) == 3:
                    name, marks, grade = row
                    print(f"{name:<20} {marks:<10} {grade:<10}")
                    has_records = True
                    
            if not has_records:
                print("No student records found below the header.")
            print(f"{'='*40}\n")
            
    except FileNotFoundError:
        # Handles cases where the user tries to view data before adding any students
        print(f"Notice: No records found. The file '{FILE_NAME}' does not exist yet.\n")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}\n")

def search_student():
    """Searches for a specific student by name in the CSV file."""
    search_name = input("Enter the student name to search: ").strip()
    if not search_name:
        print("Error: Search query cannot be empty.\n")
        return

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            
            # Skip the header row if present
            try:
                next(reader)
            except StopIteration:
                print("\nThe gradebook file is empty.\n")
                return
                
            found = False
            for row in reader:
                if len(row) == 3:
                    name, marks, grade = row
                    # Fixed: Standardized lower-case normalization for a foolproof case-insensitive check
                    if name.strip().casefold() == search_name.casefold():
                        print(f"\nStudent Found:")
                        print(f"Name  : {name}")
                        print(f"Marks : {marks}")
                        print(f"Grade : {grade}\n")
                        found = True
                        break # Exit loop early once a match is found
                        
            if not found:
                print(f"\nRecord not found for student matching '{search_name}'.\n")
                
    except FileNotFoundError:
        print(f"Notice: No records found. The file '{FILE_NAME}' does not exist yet.\n")
    except Exception as e:
        print(f"An unexpected error occurred while searching: {e}\n")

def main():
    """Main application loop to drive the user interface menu."""
    while True:
        print("=== Student Gradebook Menu ===")
        print("1. Add Student")
        print("2. View Student Records")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_records()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting Student Gradebook App. Data safely saved. Goodbye!")
            break
        else:
            print("\nInvalid selection! Please input a valid option number from 1 to 4.\n")

if __name__ == "__main__":
    main()
