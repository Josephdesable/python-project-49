import prompt
import random


def even_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_answer = 0
    for i in range(3):
        num = random.randint(1, 100)
        print('Question:', num)
        answer = prompt.string('Your answer: ')
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            counter_answer += 1
            print('Correct!')
        else:
            if num % 2 == 0 and answer != 'yes':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again,", name + '!')
                return False
            elif num % 2 != 0 and answer != 'no':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again,", name + '!')
                return False
    if counter_answer == 3:
        print('Congratulations,', name + '!')
        return True


def main():
    even_check()


if __name__ == "__main__":
    main()
