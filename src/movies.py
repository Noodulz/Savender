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
    n = 1
    if (len(search) > 5):
        print("\n")
        for q in range(0, 5):
            print(str(n) + ". " + search[q].title)
            print(search[q].overview)
            n += 1
            print("\n")
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
    recommendations = movie.recommendations(movie_id=id)
    movies = []
    time.sleep(0.5)
    print("\n")
    print(colored("Found!", 'red'))
    print(colored("We recommended the following movies: \n", 'red'))
    for i in range(0, 5):
        print(colored(recommendations[i].title, 'magenta'))
    userInput = input("\nPress Enter to Continue...")

if __name__ == '__main__':
    main()
