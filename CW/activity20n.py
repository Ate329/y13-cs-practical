def test_try_exepct():
    while True:
        try:
            integer = int(input("Enter an integer: "))
            print(f"You entered: {integer}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt \nProgram stopped")
            break
        else:
            print("Thank you for entering a valid integer.")

def main():
    test_try_exepct()

if __name__ == "__main__":
    main()
