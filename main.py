from pyscript import document

# This function runs when the button is clicked
def validate_account(event):

    # Get the value entered in the username input field
    username = document.getElementById("username").value

    # Get the value entered in the password input field
    password = document.getElementById("password").value

    # Get the result <div> where messages will be displayed
    result = document.getElementById("result")

    # Create an empty list to store error messages
    messages = []


    # -------------------------
    # USERNAME VALIDATION
    # -------------------------

    # Check if username length is less than 7 characters
    if len(username) < 7:

        # Calculate how many characters are needed
        remaining = 7 - len(username)

        # Add message to the list
        messages.append(f"Username needs {remaining} more character(s).")


    # -------------------------
    # PASSWORD LENGTH CHECK
    # -------------------------

    # Check if password length is less than 10 characters
    if len(password) < 10:

        # Calculate how many characters are needed
        remaining = 10 - len(password)

        # Add message to the list
        messages.append(f"Password needs {remaining} more character(s).")


    # -------------------------
    # PASSWORD LETTER CHECK
    # -------------------------

    # Count how many letters are inside the password
    # char.isalpha() returns True if the character is a letter
    # char is short for character
    letter_count = sum(1 for char in password if char.isalpha())

    # If there are no letters
    if letter_count < 1:
        messages.append("Password needs at least 1 letter.")


    # -------------------------
    # PASSWORD NUMBER CHECK
    # -------------------------

    # Count how many digits are inside the password
    # char.isdigit() returns True if the character is a number
    number_count = sum(1 for char in password if char.isdigit())

    # If there are no numbers
    if number_count < 1:
        messages.append("Password needs at least 1 number.")


    # -------------------------
    # FINAL RESULT DISPLAY
    # -------------------------

    # If there are any messages in the list,
    # it means some requirements are not satisfied
    if messages:

        # Apply Bootstrap styling for error (red text)
        result.className = "mt-3 text-danger fw-bold"

        # Join all error messages into one string with line breaks
        result.innerHTML = "<br>".join(messages)

    else:
        # If no errors, it means all conditions are satisfied

        # Apply success styling (green text)
        result.className = "mt-3 text-success fw-bold"

        # Display success message
        result.innerHTML = "Account successfully created!"