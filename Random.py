import time

def random_number(x,y):
    """
    Generates a random number between x and y. 
    """
   sub=y-x
   random=int(time.time()*1000)
   random = random % sub
   random = random + x
   return random

x=int(input())
y=int(input())
