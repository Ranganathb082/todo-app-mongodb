# Define a customizable default value
default_value = "abcdef"

# Generate the custom message
custom_message = f"Enter a value (or press Enter to use the default '{default_value}'): "

# Get user input with a customizable default value
user_input = input(custom_message) or default_value

# Use the user's input (or the default value)
print(f"You entered: {user_input}")
