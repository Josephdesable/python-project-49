import prompt
import random
def nod():
	counter_nod = 0
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello,', name + '!')
	print('Find the greatest common divisor of given numbers.')
	for _ in range(3):
		number_nod1 = random.randint(1, 100)
		number_nod2 = random.randint(1, 100)
		total_nod = 0
		for i in range(1, max(number_nod1, number_nod2)):
			if number_nod1%i == 0 and number_nod2%i == 0:
				total_nod = i
		print('Question:', number_nod1, number_nod2)
		answer = prompt.string('Your answer: ')
		if str(answer) == str(total_nod):
			counter_nod += 1
			print('Correct!')
		if str(answer) != str(total_nod):
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{total_nod}'.")
			print("Let's try again,", name + '!')
			return False
	if counter_nod == 3:
		print('Congratulations,', name + '!')
		return True
def main():
    nod()    
if __name__ == "__main__":  
    nod()

