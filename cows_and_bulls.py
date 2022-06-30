#import randint from random module to pick random integer
from random import randint
def random():
  while True:
    #converting random integer to string
    n = str(randint(100,999))
#condition for not repeating same number in random integer
    if not(n[0] == n[1] or n[1] == n[2] or n[0] == n[2]):
#returning the random integer to n
      return n
#taking name as input from the user
name = input("welcome to the cows and bulls game\nplease enter user name.")
print("hi",name)
#assigning values to chances, cows, and bulls
chances = 10
cows = 0
bulls = 0
#creating object to the random function and converting it to string
num = str(random())
while chances > 0:
  print("you  have",chances,"chances left.")
#taking input as a guess from the user
  n = str(input("Enter your guess"))
#checking if user has guess the correct value matching random integer
  if num == n:
    print("Great! you got it right.")
    #if user guessed the value correct then break the loop
    break
#if user not guessed wrong inter then loop through the number to find bulls and cows
  else:
    for i in range(0,3):
      if n[i] == num[i]:
#if position of the number is matched then increment the bull by 1
        bulls = bulls + 1
      elif n[i] in num:
#if certain number is matched from random integer then increment cow by 1
        cows = cows + 1
    print("keep going. you have",bulls,"bulls and",cows,"cows.")
#after each chance reset the values of cows and bulls and decrement chance by 1
    bulls = 0
    cows = 0
    chances = chances - 1
#if user failed to guess after all chances then print the random number
print("The correct ans is",num)
