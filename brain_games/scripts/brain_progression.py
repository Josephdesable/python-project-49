import prompt
import random


def generate_progression(start, end, step, missing_index):
    progression = []
    current_value = start
    for _ in range(end - start):
        progression.append(current_value)
        current_value += step
    progression[missing_index] = '..'
    return progression


def ask_question(progression):
    print('Question:', ' '.join(map(str, progression)))
    return prompt.string('Your answer: ')


def is_arithmetic(progression):
    differences = [progression[i + 1] - progression[i]
                   for i in range(len(progression) - 1)]
    return len(set(differences)) == 1


def progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('What number is missing in the progression?')

    counter_progression = 0
    for _ in range(3):
        start = random.randint(1, 20)
        end = random.randint(start + 10, 100)
        length = random.randint(5, 10)
        step = (end - start) // length
        missing_index = random.randint(0, length - 1)

        progression = generate_progression(start, end, step, missing_index)
        answer = ask_question(progression)

        if int(answer) == start + step * missing_index:
            counter_progression += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;"
                f"(. Correct answer was '{start + step * missing_index}'.")
            print("Let's try again,", name + '!')
            return False

    print('Congratulations,', name + '!')
    return True


def main():
    progression()


if __name__ == "__main__":
    main()
