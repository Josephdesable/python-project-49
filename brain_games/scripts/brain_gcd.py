import prompt
import random


def nod(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def main():
    counter_nod = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        number_nod1 = random.randint(1, 100)
        number_nod2 = random.randint(1, 100)
        total_nod = nod(number_nod1, number_nod2)
        print('Question:', number_nod1, number_nod2)
        answer = prompt.string('Your answer: ')
        if str(answer) == str(total_nod):
            counter_nod += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;"
                f"(. Correct answer was '{total_nod}'.")
            print("Let's try again,", name + '!')
            return False
    if counter_nod == 3:
        print('Congratulations,', name + '!')
        return True


if __name__ == "__main__":
    main()
