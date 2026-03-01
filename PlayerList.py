from pyscript import document, display


def PlayersList(e): #Whenever the user presses the button, this event will be conducted.

    document.getElementById('List_Players').innerHTML = '' #To reset the message whenever the user clicks the button so it doesn't duplicate.

    players = ["Ebtisam Al Hazmi", "Ya  niszolt Alvarez", "Giana Bernas", "Ethan Belsa", "Julianna Calaycay", "Jamila Castelo", "Francesca Cruz", "Ely Defensor", "Danielle Dimasuhid", "Althea Francisco", "Denise Juatchon", "Judah Judge", "Cristina Hsu", 'Geoffrey Lilagan', 'Sam Luna', 'Josh Macaranas', 'Pain Mateo', 'Ashley Mondragon', 'Lance Naldoza', 'Gabriel Natividad', 'Sofia Ng', 'Hendrich Ong', 'Trisha Paz', 'Miguel Ramos', 'Queeny Ramos', 'Samantha Ramos', 'Ashlei Reodica', 'Vaughn Repolona'] #This is used for the names of the players in a list data type, as the items in this list will be used in the 'for i' loop to enumerate them.

    for i, player in enumerate(players, start=1): #To get the names in the players variable using, and enumerates the list from 1 until the last item in the variable.
        display(f"{i}. {player}", target='List_Players') #To display the order of the player and the name using f string and their variable names based on positioning.