class Greeting:
    def hello(self, first_name=None, last_name=None):
        if first_name is None and last_name is None:
            print("Hello!")
        elif last_name is None:
            print(f"Hello, {first_name}!")
        else:
            print(f"Hello, {first_name} {last_name}!")

greeter = Greeting()

greeter.hello()                  
greeter.hello("Alice")           
greeter.hello("Alice", "Smith")