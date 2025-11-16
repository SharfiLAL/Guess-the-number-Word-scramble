'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

'''
"Guess the Number"

import random
x = random.randint(1, 10)
#I have used the random module to select a number between 1 and 10.
Guess = int(input("Guess the number : "))
#I define Guess as an integer to be able to guess the number between 1 and 10.
while x != Guess:
 if Guess > x:
  print("Too High")
  print("Guess again")
  Guess = int(input("Guess the number : "))
#I have set up a loop for when the player guesses a number which is too high.
 elif Guess < x:
  print("Too Low")
  print("Guess again")
  Guess = int(input("Guess the number : "))
#the loop continues for when the player guesses a number which is too low.
 else: Guess = x
print("Correct guess")
#finally when the player guesses the correct number, this is printed.
'''

"Words scramble"

import random
x = random.choice(['python', 'java', 'javascript', 'automation', 'pytest', 'guvi', 'selenium'])
#I have used the random module to randomly select a word from the list I have created
Selected_word = list(x)
#I have made list of the characters of the word which Python randomly selected
random.shuffle(Selected_word)
#The above line will let Python scramble the selected word which will then be displayed
print(Selected_word)
Guess_the_scrambled_word = str(input("Guess the scrambled word : "))
#I define a string for the player to know that they can start guessing the word
Scrambled_word = "".join(x)
#with this function I ask of Python to put the characters of the word back to its original state
#a loop is then initiated so the player can start playing or guessing
while Scrambled_word != Guess_the_scrambled_word:
  print("Incorrect guess")
  print("Guess again")
  Guess_the_scrambled_word = str(input("Guess the scrambled word : "))
#I have created a loop in order for the player to guess the scrambled word
else: Guess_the_scrambled_word = Scrambled_word
print("Correct guess")
#Finally when the guess is correct, "Correct guess" is displayed