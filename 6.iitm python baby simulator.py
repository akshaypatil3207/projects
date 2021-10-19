#written by Akshay patil
#import random as r
from random import choice
questions=["why sky is blue ? ","why animals don't talk ? ","why are you crying ? ","where is mommy ? ", "why do you go to school ? ","are ghosts real ? ", " is there ghost on our terrace at night ? "]
#answer=input("{}".format(questions[r.randint(0,7)])).lower()
answer=input("{}".format(choice(questions))).lower()

while answer != "just because" :
    answer=input("why?  ").lower()  #why
    if  answer == "just because" :  print("ok")

    
    
    
    
    

