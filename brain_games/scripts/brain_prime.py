import prompt
import random


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_random_number():
    return random.randint(2, 100)


def ask_question(number):
    print('Question:', number)
    return prompt.string('Your answer: ')


def check_answer(answer, number):
    if (answer == 'yes' and is_prime(number)) or \
            (answer == 'no' and not is_prime(number)):
        print('Correct!')
        return True
    return False


def easy_number():
    counter_number = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = get_random_number()
        answer = ask_question(number)
        if check_answer(answer, number):
            counter_number += 1
        else:
            correct_answer = 'yes' if is_prime(number) else 'no'
            print(
                f"'{answer}' is wrong answer ;"
                f"(. Correct answer was '{correct_answer}'.")
            print("Let's try again,", name + '!')
            return False
    print('Congratulations,', name + '!')
    return True


def main():
    easy_number()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
