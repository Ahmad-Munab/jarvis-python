# Define a global variable called context and assign it an empty dictionary
context = {
    "chat_history": [],
    "commands_history": []
}

# Define a function to update the context with new key-value pairs
def update(**kwargs):
    # Use the global keyword to access the global variable context
    global context
    # Loop through the keyword arguments and add them to the context dictionary
    for key, value in kwargs.items():
        context[key] = value

# Define a function to get the value of a key from the context
def get(key):
    # Use the global keyword to access the global variable context
    global context
    # Return the value of the key from the context dictionary, or None if the key is not found
    return context.get(key) 
