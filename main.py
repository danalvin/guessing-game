import random


def checkGuess(secret, guess):

    if secret == guess:
        return(0)
    elif secret > guess:
        return(1)
    else:
        return(-1)

def main():
    print('please input your username')
    username=input()
    score=int(0)
    secret=int(len(username)+ (random.randint(0,10)))
    guesses=0

    print(f'Hello {username},  welcome to the guessing game')

    for i in range(5, 8):
        remaining= (3-guesses)
        print(f"you have {remaining} gueses left")
        print('what is your guess?')
        guess = int(input())
        guesses = guesses + 1
        result = checkGuess(secret, guess)
        if result == 0 :
            if guesses == 1:
                print('Amazing, On your first guess!')
                score = score + 10
            elif guesses == 2:
                print('Amazing, On your second guess!')
                score = score + 5
            else:
                print('Lucky, On your third guess!')
                score = score + 1
        else:
            if result == 1:
                    print(f'Your guess, {guess}, was too low!')
            else:
                print(f'Your guess, {guess}, was too high!')

        if guesses == 3:
            break

    print(f'Thank you for playing {username}, your score was {score} points') 

if __name__ == "__main__":
    main()