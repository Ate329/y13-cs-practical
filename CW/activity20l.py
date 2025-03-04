import pickle

class student():
    def __init__(self):
        self.name = None
        self.dateofbirth = None

def read(filename):
    with open(filename, "rb") as file:
        print(pickle.load(file))
        file.close()

def write(filename, record):
    with open(filename, "w+b") as file:
        pickle.dump(record, file)
        file.close()

student_info = student()
student_info.name, student_info.dateofbirth = "uiiai", "2020/20/20"

write("uiiai", student_info)
read("uiiai")