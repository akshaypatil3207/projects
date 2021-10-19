#written by akshay patil
known_users=['akshay','bob','rutuja','pooja','mak','yuvi']

while True:
    print("Hii! my name is Travis")
    name=input("what is your name? :- ").strip()

    if name.lower() in known_users:
        print("Welcome {}.".format(name))
        remove=input("Would you like to be removed from the system (y/n)?:").lower()
        if remove == "y":
            known_users.remove(name)
        else:
            print("No worries, see you around")
           
       
    else:
        print("Hmmm i don't think i have met you yet {}".format(name))
        add_me=input("Would you like to be added to the system (y/n)?:-").strip().lower()
        if add_me=="y" :
            known_users.append(name)
        else:
            print("No worries, see you around")
        
        
