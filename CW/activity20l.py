import pickle

class Student:  # Changed to PascalCase naming convention for classes
    def __init__(self):
        self.name = None
        self.dateofbirth = None

    def __str__(self):  # Added __str__ method for better printing
        return f"Name: {self.name}, Date of Birth: {self.dateofbirth}"

def read(filename):
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
            print(data)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error reading file: {e}")

def write(filename, record):
    try:
        with open(filename, "wb") as file:  # Changed w+b to wb
            pickle.dump(record, file)
    except Exception as e:
        print(f"Error writing to file: {e}")

# Create and populate student info
student_info = Student()
student_info.name = "uiiai"
student_info.dateofbirth = "2020/20/20"

# Add file extension for better practice
filename = "uiiai.dat"

# Write and read the file
write(filename, student_info)
read(filename)
