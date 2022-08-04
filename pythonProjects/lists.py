games = []
digital_movies=[]
dvd=[]
movies = [digital_movies, dvd]


print("Welcome to the Movie Lists: ")

while True:
    print("What would you like to add? Movie or Game?")
    type = input()

    print(f"Please enter the title of this {type}:")
    title = input( )

    if type == "Movie":
        print("Is this a DVD or Digital movie? ")
        type_movie = input()
        if type_movie == "DVD":
            dvd.append(title)
        else:
            digital_movies.append(title)
    else:
        games.append(title)

    print("Would you like to add anything else? y/n")
    again = input()

    if again == "n":
        print("Before you leave, these are the items in you Movie and Game Lists. ")
        for item in dvd:
            print(f"DVD: {item}")
        for item in digital_movies:
            print(f"Digital Movie: {item}")
        for item in games:
            print(f"Game: {item}")
        break