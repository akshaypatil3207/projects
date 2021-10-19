# written by akshay patil
import random
health = 50
difficulty=int(input("Enter difficulty as 1,2,3 :- "))
potion_health=int(random.randint(40,50)/difficulty)
health += potion_health
print(health)


