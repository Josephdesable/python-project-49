import prompt
import random
def calculate():
	counter_answer = 0
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello,', name + '!') 
	print('What is the result of the expression?')
	for _ in range(3):
		number_generate1 = random.randint(1, 100)
		number_generate2 = random.randint(1, 100)
		generate_symbol_array = ['+', '-', '*']
		generate_symbol = random.choice(generate_symbol_array)
		math_dict = {'+': number_generate1 + number_generate2, '-': number_generate1 - 			number_generate2, '*': number_generate1 * number_generate2}
		result = math_dict[generate_symbol]
		print(f'Question: {number_generate1} {generate_symbol} {number_generate2}')
		answer = prompt.string('Your answer: ')
		if str(answer) == str(result):
			counter_answer += 1
			print('Correct!')
		if str(answer) != str(result):
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
			print("Let's try again,", name + '!')
			return False
	if counter_answer ==3:
		print('Congratulations,', name + '!')
		return True

def main():
    calculate()     
if __name__ == "__main__":  
    main()

