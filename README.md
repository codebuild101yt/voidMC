


# VoidMC

## Overview

The Minecraft Bukkit Plugin Compiler is a tool designed to convert a custom plugin syntax into a JAR file suitable for use in Minecraft servers. This compiler allows users to define plugins using a simplified syntax that is then translated into Java code.

## Features

- **Custom Syntax**: Write plugins using an intuitive syntax.
- **Function Definitions**: Define functions and Minecraft event handlers.
- **Control Flow**: Use loops, conditionals, and exception handling.
- **Data Structures**: Utilize lists, dictionaries, sets, and tuples.
- **Import Modules**: Import other modules and libraries as needed.
- **Comments**: Support for single-line and multi-line comments.
- **File Handling**: Read from and write to files.
- **Type Hinting**: Provide type hints for function parameters and return types.

## Syntax Overview

### Plugin Metadata

Define the metadata for your plugin.

```plaintext
Plugin:
    #info
    name: "example plugin"          # Name of the plugin
    version: "1.0"                  # Plugin version
    author: "Grayson"               # Author of the plugin
    Minecraft version: "1.21"       # Compatible Minecraft version
```

### Functions

Define functions for your plugin.

```plaintext
func [variables](name):
    # Runs like a function
    return [value]  # Return a value from the function
```

### Control Flow

Use conditionals to control the flow of your program.

```plaintext
if [variable] = [true/false/specific value]:
    # Code if condition is true
elif [condition]:
    # Code if the second condition is true
else:
    # Code if none of the above conditions are true
```

### Minecraft Functions

Define Minecraft-specific functions to handle events.

```plaintext
def on_player_join(player):
    # Code to run when a player joins
    print(f"{player.name} has joined the game!")  # Send message to chat

def on_player_leave(player):
    # Code to run when a player leaves
    print(f"{player.name} has left the game!")  # Send message to chat

def spawn_entity(entity_type, location):
    # Code to spawn an entity
    print(f"Spawning {entity_type} at {location}.")  # Send message to chat

def give_item(player, item, quantity):
    # Code to give an item to a player
    print(f"Gave {quantity} {item} to {player.name}.")  # Send message to chat

def send_message(player, message):
    # Code to send a message to a player
    print(f"Message to {player.name}: {message}")  # Send message to chat
```

### Data Structures

Initialize various data structures.

```plaintext
list = [item1, item2, item3]                    # List initialization
dict = {key1: value1, key2: value2}            # Dictionary initialization
set = {item1, item2, item3}                      # Set initialization
tuple = (item1, item2, item3)                    # Tuple initialization
```

### Looping

Use loops to iterate over collections.

```plaintext
for item in list:
    # Iterate over each item in the list
    print(item)  # Print the current item to chat

while [condition]:
    # Continue looping while the condition is true
    if [break_condition]:
        break  # Exit the loop
```

### Exception Handling

Handle exceptions gracefully.

```plaintext
try:
    # Code that might throw an exception
    risky_operation()
except [ExceptionType] as e:
    # Handle the exception
    print("An error occurred:", e)  # Send error message to chat
finally:
    # Code that runs regardless of exception
    cleanup()
```

### Importing Modules

Import external modules as needed.

```plaintext
import [module_name]  # Import a module
```

### Classes and Objects

Define classes and instantiate objects.

```plaintext
class [ClassName]:
    def __init__(self, [parameters]):
        # Constructor code
        self.attribute = [value]  # Set an instance attribute

    def [method_name](self, [parameters]):
        # Method code
        return self.attribute  # Return an instance attribute
```

### Inheritance

Create subclasses that inherit from parent classes.

```plaintext
class [ChildClass]([ParentClass]):
    def __init__(self, [parameters]):
        super().__init__([parameters])  # Call the parent constructor

    def [method_name](self):
        # Override a parent method
        super().[method_name]()  # Call the parent method
```

### Comments

Add comments to your code.

```plaintext
# This is a single line comment

"""
This is a
multi-line comment
"""
```

### Input and Output

Get user input and display output.

```plaintext
user_input = input("Enter a value: ")  # Get user input
print("You entered:", user_input)  # Print user input to chat
```

### Lambda Functions

Define anonymous functions.

```plaintext
lambda_function = lambda x: x * 2  # Anonymous function
```

### List Comprehensions

Create lists using comprehensions.

```plaintext
squared_list = [x * x for x in range(10)]  # Create a list of squares
```

### Decorators

Define and use decorators.

```plaintext
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")  # Send message to chat
```

### File Handling

Read from and write to files.

```plaintext
with open('file.txt', 'r') as file:
    content = file.read()  # Read file content
```

### Generators

Create generator functions for yielding values.

```plaintext
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)  # Iterate over generator values and send to chat
```

### Regular Expressions

Use regular expressions for pattern matching.

```plaintext
import re
pattern = r'\d+'  # Regex pattern for digits
matches = re.findall(pattern, "123 and 456")  # Find all matches
```

### Type Hinting

Provide type hints for function parameters and return types.

```plaintext
def add_numbers(a: int, b: int) -> int:
    return a + b  # Function with type hints
```

### Slicing

Access parts of sequences using slicing.

```plaintext
my_list = [1, 2, 3, 4, 5]
sub_list = my_list[1:4]  # Get a slice of the list
```

### Conditional Expressions

Use inline if-else statements.

```plaintext
result = "Even" if x % 2 == 0 else "Odd"  # Inline if-else statement
```

## Usage

1. Write your plugin code using the defined syntax in a file (e.g., `main.void`).
2. Run the compiler script:

   ```bash
   python compiler.py main.void
   ```

3. The output will be a JAR file ready to be used in a Minecraft server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## Contact

For questions or feedback, please contact Grayson at graytalbot16@gmail.com].


Feel free to customize this documentation further to suit your project, such as adding examples or clarifying specific commands! If you need more assistance, just let me know.
