import prompt
import random

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
        progression_array = [i for i in range(start, end, step)]
        index = random.randint(0, len(progression_array)-1)
        progression_array_copy = progression_array.copy()
        progression_array[index] = '..'
        result =  ' '.join(map(str, progression_array))
        print('Question:', result)
        answer = prompt.string('Your answer: ')

        if index == 0:
            if progression_array[1] - int(answer) == progression_array[2] - progression_array[1]:
                counter_progression += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{progression_array_copy[index]}'.")
                print("Let's try again,", name + '!')
                return False
        elif index == len(progression_array) - 1:
            if  int(answer) - progression_array[-2] == progression_array[-2] - progression_array[-3]:
                counter_progression += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{progression_array_copy[index]}'.")
                print("Let's try again,", name + '!')
                return False
        else:
            if (abs(int(answer) - progression_array[index - 1]) == abs(int(answer) - progression_array[index + 1])):
                counter_progression += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{progression_array_copy[index]}'.")
                print("Let's try again,", name + '!')
                return False

    if counter_progression == 3:
        print('Congratulations,', name + '!')

def main():
    progression()       
if __name__ == "__main__":  
    main()





