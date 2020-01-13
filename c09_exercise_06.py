"""
6. In Repetition Based on User Input, on page 162, you saw a loop that prompted
users until they typed quit. This code won’t work if users type Quit, or QUIT,
or any other version that isn’t exactly quit. Modify that loop so that it
terminates if a user types that word with any capitalization.
"""

text = ""

while text.lower() != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text.lower() == "quit":
        print("…exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")
