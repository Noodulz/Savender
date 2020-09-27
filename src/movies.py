from tmdbv3api import TMDb
from tmdbv3api import Movie
from termcolor import colored, cprint
import time
import config


tmdb = TMDb()
tmdb.api_key = config.tmdb_key
tmdb.language = 'en'
movie = Movie()

def search(inputer):
    search = movie.search(inputer)
    chosenID = 0
    n = 1
    if (len(search) > 5):
        print("\n")
        for q in range(0, 5):
            print(str(n) + ". " + search[q].title)
            print(search[q].overview)
            n += 1
            print("\n")
        num = int(input("Enter a number: "))
        chosenID = search[num-1].id
        return chosenID
    elif(len(search) <= 0):
        return chosenID
    else:
        print("\n")
        for r in range(0, len(search)):
            print(str(n) + ". " + search[r].title)
            print(search[r].overview)
            n += 1
            print("\n")
        num = int(input("Enter a number: "))
        chosenID = search[num-1].id
        return chosenID

def main():
    userInput = input(colored("\nEnter a movie: ", 'green'))
    id = search(userInput)
    movies = []
    time.sleep(0.5)
    if (id == 0):
        print(colored("\nSorry! Could not find your recommendations or your results\n", 'magenta'))
    else:
        recommendations = movie.recommendations(movie_id=id)
        print("\n")
        print(colored("Found!", 'red'))
        print(colored("We recommended the following movies: \n", 'red'))
        for i in range(0, 5):
            print(colored(recommendations[i].title, 'magenta'))
        print("\n")
    userInput = input("Press Enter to Continue...")

if __name__ == '__main__':
    main()
