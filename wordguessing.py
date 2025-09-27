import random
word = ['water', 'lemon' , 'rice', 'mutton' , 'five','six']
result =random.choice(word)

guessword = ['_'] *len(result)
attempts = 10

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessword))

  guess = input('Guess a letter: ').lower()
   
  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessword[i] = guess
        print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessword:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessword:
  print('\nYou\'ve run out of attempts! The word was: ' + word)
    