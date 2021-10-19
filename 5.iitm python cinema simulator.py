#written by Akshay patil
#load available films
movies={
    "Bahubali":{"min_age":"5","seats":4,"price":150},
    "Lust":{"min_age":"18","seats":4,"price":200},
    "Jism":{"min_age":"18","seats":4,"price":250},
    "Ludo":{"min_age":"5","seats":4,"price":120},
    "Ghost Busters":{"min_age":"5","seats":4,"price":200},
    }

#show available films to user

while True:
    print("   ")
    print("  Hello there, Welcome to Inox. These are the movies available today")
    print(list(movies.keys()))
    print("   ")

    #ask user to pick a film
    
    movie=input("  Which movie would you like to watch ?  ").strip().title()
    if movie in movies :
        
        # ask for users age
        
        age=input("  What is your age ?  ").strip()
        print("   ")
        
        #if age is appropriate and there are enough seats availbale then the progrogram will allow the person else it will then that age is less or seats are not available

        if int(age) > int(movies[movie]["min_age"]) and movies[movie]["seats"]>0 :
            print("  ok, please pay {}  ".format(movies[movie]["price"]))
            movies[movie]["seats"]-=1
         #   print(movies[movie]["seats"])
        elif int(movies[movie]["seats"]) == 0:
            print("  Sorry, Seats are full. ")
        else:
            print("  Sorry you are minor to watch this film, please come back when you grow up")
            
        
    else:   print("  I am really sorry, That movie is not available.  ")










