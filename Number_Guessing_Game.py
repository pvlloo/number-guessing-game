import random


print('\n🎮 Welcome to the number guessing game! 🎮\n')

print("\nI'm thinking of a number between 1 and 100.")
print('You can choose the difficulty level wich will determine the number of attempts you have to guess the number.\n')

while True:

     print('\nPlease select a difficulty level:')
     print('1. Easy (10 attempts)')
     print('2. Medium (7 attempts)')
     print('3. Hard (5 attempts)\n')



     difficulty_level = input('\nEnter your choice (1-3): ')



     while difficulty_level not in ['1', '2', '3']:
         print('Invalid choice. Please enter a valid difficulty level.')
         difficulty_level = input('Enter your choice (1-3): ')




     print('You have selected difficulty level:', difficulty_level)

     if difficulty_level == '1':
             max_attempts = 10
     elif difficulty_level == '2':
             max_attempts = 7
     else:
             max_attempts = 5



     secret_number = random.randint(1, 100)
     attempts = 1
 

     guess = input('\nGuess a number between 1 and 100: ')




     while not guess.isdigit() or (int(guess) < 1 or int(guess) > 100):
         print('\nChoose a valid number. \n')
         guess = input('\nGuess a number between 1 and 100: ')

     guess = int(guess)



            
     while guess != secret_number and attempts < max_attempts:
         
         if guess < secret_number:
             print('\nThe secret number is greater than your guess. \n')
         else:
             print('\nThe secret number is less than your guess. \n')

         attempts += 1

         guess = input('\nGuess a number between 1 and 100: ')

         while not guess.isdigit() or (int(guess) < 1 or int(guess) > 100):
             print('\nChoose a valid number. \n')
             guess = input('\nGuess a number between 1 and 100: ')

         guess = int(guess)






     if guess == secret_number:
         print(f'\nCongratulations! You guessed the number in {attempts} attempts!\n')
     else:
         print(f'\nSorry, you ran out of attempts. The secret number was {secret_number}.\n')





     answer = input('\nDo you want to play again? (yes/no): ')
 

     if answer == 'no':
        print('Thanks for playing!\n')
        break