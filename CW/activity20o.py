def test_OSError():
    try:
        studentFile = open('students.csv123', 'rb')
    except OSError:
        print("file does not exist")

def test_os_exist():
    import os
    if os.path.exists('students.csv'):
        print("file exists")
    else:
        print("file doesnt exist")

def main():
    test_OSError()
    test_os_exist()

if __name__ == "__main__":
    main()
