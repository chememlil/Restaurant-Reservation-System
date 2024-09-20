#function to clear the terminal screen
def clear_screen():
    #importing os module to interact with the operating system
    import os
    #Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

#Function to get input from the user with optional typing casting
def get_input(prompt, cast_type=str):
    # Loop until valid input is provided
    while True:
        try:
            # Get input from the user and cast it to the specified type (default is string)
            return cast_type(input(prompt))
        except ValueError:
            # If the input cannot be cast to the specified type, show an error and prompt again
            print("Invalid input. Please try again.")
