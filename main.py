from pyscript import document

# ------------------------------------------------------------
# set_theme(team)
# What it does:
# - Changes the PAGE background color and the BUTTON color
#   based on the team name.
#
# Why we need it:
# - So when a student becomes eligible and gets a team,
#   the website "matches" the team color (blue/red/yellow/green).
#
# How it works:
# 1) Start with default colors (used for reset / no team).
# 2) If the team matches one of the team names, replace the colors.
# 3) Apply the colors to the webpage using document + style.
# ------------------------------------------------------------
def set_theme(team):
    # Default theme (neutral background, blue button)
    body_color = "#f8fafc"
    btn_color = "#0d6efd"
    btn_text = "white"

    # Team-based themes
    if team == "Blue Bears":
        body_color = "#1d4ed8"
        btn_color = "#1e40af"
        btn_text = "white"
    elif team == "Red Bulldogs":
        body_color = "#dc2626"
        btn_color = "#b91c1c"
        btn_text = "white"
    elif team == "Yellow Tigers":
        body_color = "#facc15"
        btn_color = "#eab308"
        btn_text = "black"   # black text is easier to read on yellow
    elif team == "Green Hornets":
        body_color = "#16a34a"
        btn_color = "#15803d"
        btn_text = "white"

    # Apply background color to the whole page.
    # (The smooth fade is handled by CSS transition in index.html.)
    document.body.style.backgroundColor = body_color

    # Apply colors to the button.
    # IMPORTANT: Your HTML button must have id="checkBtn".
    btn = document.getElementById("checkBtn")
    btn.style.backgroundColor = btn_color
    btn.style.borderColor = btn_color
    btn.style.color = btn_text


# ------------------------------------------------------------
# check_student(event=None)
# What it does:
# - Reads the form inputs (registration, medical, grade, section).
# - Checks eligibility rules:
#   a) Must be registered online
#   b) Must have medical clearance
#   c) Must be Grade 7–10
# - If NOT eligible, shows the correct instruction message.
# - If eligible, assigns a team and shows:
#   - A congratulatory message
#   - The assigned team
#   - Updates the theme colors to match the team
#
# event=None:
# - PyScript may pass a click event automatically.
# - event=None keeps the function working either way.
# ------------------------------------------------------------
def check_student(event=None):
    # Read values from the HTML elements using their IDs
    reg_value = document.getElementById("registered").value
    med_value = document.getElementById("medical").value
    grade_text = document.getElementById("grade").value

    # Section is required in the form but not used in team assignment.
    # (We still read it to match the project requirement.)
    section_text = document.getElementById("section").value

    # Convert "yes"/"no" into True/False
    registered = (reg_value == "yes")
    medical = (med_value == "yes")

    # -------------------------
    # 1) Validate the grade input
    # -------------------------
    # If nothing was typed, we cannot continue.
    if grade_text == "":
        document.getElementById("result").innerText = "Please enter your grade level."
        set_theme("")  # reset to default theme
        return

    # .isdigit() checks if the input contains only digits (0–9).
    # If not, it means the user typed letters/symbols.
    if not grade_text.isdigit():
        document.getElementById("result").innerText = "Invalid input. Grade must be a number."
        set_theme("")  # reset to default theme
        return

    # Convert the valid grade text into an integer number
    grade = int(grade_text)

    # -------------------------
    # 2) Eligibility checks (based on rules)
    # -------------------------
    # Rule a: must be registered online
    if not registered:
        document.getElementById("result").innerText = "Not eligible: Please register online."
        set_theme("")  # reset to default theme
        return

    # Rule b: must have medical clearance
    if not medical:
        document.getElementById("result").innerText = "Not eligible: Please secure a medical clearance."
        set_theme("")  # reset to default theme
        return

    # Rule c: grade must be 7 to 10
    if grade < 7 or grade > 10:
        document.getElementById("result").innerText = "Not eligible: Only Grade 7 to Grade 10 students are eligible."
        set_theme("")  # reset to default theme
        return

    # -------------------------
    # 3) Team assignment (simple and easy to explain)
    # -------------------------
    # Grade 7 → Blue Bears
    # Grade 8 → Red Bulldogs
    # Grade 9 → Yellow Tigers
    # Grade 10 → Green Hornets
    if grade == 7:
        team = "Blue Bears"
    elif grade == 8:
        team = "Red Bulldogs"
    elif grade == 9:
        team = "Yellow Tigers"
    else:
        team = "Green Hornets"

    # Update background + button colors to match team
    set_theme(team)

    # Show success output (use \n for a new line)
    document.getElementById("result").innerText = (
        "Congratulations! You are eligible.\n"
        "Intramurals Team: " + team
    )


# ------------------------------------------------------------
# Run once when the page loads
# - Sets the default theme before the user clicks the button.
# ------------------------------------------------------------
set_theme("")
