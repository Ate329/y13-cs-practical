import csv
import os

class Student:
    def __init__(self, name, age, year, birthday):
        self.name = name
        self.age = age
        self.year = year
        self.birthday = birthday

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.year}, Birthday: {self.birthday}"

def add_student(filename):
    # Get student information from user input
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    year = input("Enter student grade: ")
    birthday = input("Enter student birthday (YYYY-MM-DD): ")
    
    student = Student(name, age, year, birthday)
    
    # Determine if we need to write the header
    file_exists = os.path.exists(filename)
    write_header = not file_exists
    
    # Append record to the CSV file using DictWriter
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ['Name', 'Age', 'Year', 'Birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if write_header:
            writer.writeheader()
        
        writer.writerow({
            'Name': student.name,
            'Age': student.age,
            'Year': student.year,
            'Birthday': student.birthday
        })
    
    print("Student record added.\n")

def search_student(filename, key_name):
    found = False
    try:
        # Open the CSV file using DictReader
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Name'].lower() == key_name.lower():
                    student = Student(row['Name'], row['Age'], row['Year'], row['Birthday'])
                    print("\nStudent record found:")
                    print(student)
                    found = True
                    break
    except FileNotFoundError:
        print("Student records file not found. Please add a record first.")
        return

    if not found:
        print("Student record not found.")

def main():
    filename = "students.csv"
    
    while True:
        print("\nMenu:")
        print("1. Add student record")
        print("2. Search student record")
        print("3. Exit")
        
        try:
            choice = input("Enter your choice: ")
            
            if choice == "1":
                add_student(filename)
            elif choice == "2":
                key_name = input("Enter student name to search: ")
                search_student(filename, key_name)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        
        except TypeError:
            print("Please enter a integer from 1, 2 and 3")
            return

if __name__ == "__main__":
    main()
